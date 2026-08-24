#!/usr/bin/env python3
"""Manage private, reproducible social-video jobs for CiudadanoInusual."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any


DEFAULT_DATA_ROOT = Path("/home/hermes/.hermes/data/ciudadanoinusual/video-jobs")
SHORT_MAX_SECONDS = 60.0
LONG_MAX_SECONDS = 15 * 60.0
SHORT_MAX_BYTES = 100 * 1024 * 1024
LONG_MAX_BYTES = 1024 * 1024 * 1024
MAX_OUTPUT_SECONDS = 60.0
MIN_OUTPUT_SECONDS = 0.5
MAX_OVERLAYS = 3
MAX_OVERLAY_CHARS = 120
MIN_ZOOM = 1.0
MAX_ZOOM = 1.35
RESERVED_DISK_BYTES = 512 * 1024 * 1024
SUPPORTED_SUFFIXES = {".mp4", ".webm", ".mov", ".avi", ".mkv", ".mpeg", ".mpg"}
SENSITIVE_PARTS = {".ssh", ".gnupg", "secrets", "credentials"}
VALID_STATES = {
    "received",
    "analyzed",
    "moment_selected",
    "rendered",
    "approved",
    "exported",
    "discarded",
    "failed",
}
ACTIVE_STATES = {"received", "analyzed", "moment_selected", "rendered", "approved", "failed"}
RETENTION_DAYS = {"discarded": 7, "failed": 7, "rendered": 30, "exported": 90}
VARIANT_KEYS = ("A", "B", "C")
SCENE_TIME_RE = re.compile(r"pts_time:([0-9]+(?:\.[0-9]+)?)")


class SocialVideoError(RuntimeError):
    """Raised when a social-video operation cannot be completed safely."""


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso_now() -> str:
    return utc_now().isoformat()


def load_preparer() -> Any:
    path = Path(__file__).with_name("preparar-video-social.py")
    spec = importlib.util.spec_from_file_location("preparar_video_social_compat", path)
    if spec is None or spec.loader is None:
        raise SocialVideoError("No se pudo cargar el preparador de video existente.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PREPARER = load_preparer()


def private_directory(path: Path, *, exist_ok: bool = False) -> None:
    path.mkdir(parents=True, exist_ok=exist_ok, mode=0o700)
    os.chmod(path, 0o700)


def write_private_json(path: Path, payload: dict[str, Any]) -> None:
    private_directory(path.parent, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as handle:
            json.dump(payload, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        os.chmod(path, 0o600)
    finally:
        temporary.unlink(missing_ok=True)


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SocialVideoError(f"No se pudo leer JSON valido: {path.name}") from exc
    if not isinstance(value, dict):
        raise SocialVideoError(f"El archivo {path.name} debe contener un objeto JSON.")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_source_path(path: Path) -> Path:
    candidate = path.expanduser()
    if candidate.is_symlink():
        raise SocialVideoError("La ruta no puede ser un enlace simbolico.")
    resolved = candidate.resolve(strict=True)
    if not resolved.is_file():
        raise SocialVideoError("La ruta debe ser un archivo de video regular.")
    if resolved.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise SocialVideoError("Formato no admitido para el flujo de video social.")
    lowered_parts = {part.lower() for part in resolved.parts}
    if lowered_parts & SENSITIVE_PARTS or resolved.name.lower().startswith(".env"):
        raise SocialVideoError("La ruta del video pertenece a una zona sensible.")
    return resolved


def validate_data_root(path: Path) -> Path:
    candidate = path.expanduser()
    if candidate.exists() and candidate.is_symlink():
        raise SocialVideoError("El almacen privado no puede ser un enlace simbolico.")
    resolved = candidate.resolve()
    if {part.lower() for part in resolved.parts} & SENSITIVE_PARTS:
        raise SocialVideoError("El almacen de video no puede estar en una zona sensible.")
    return resolved


def validate_plan_file(path: Path) -> Path:
    candidate = path.expanduser()
    if candidate.is_symlink():
        raise SocialVideoError("El plan no puede ser un enlace simbolico.")
    resolved = candidate.resolve(strict=True)
    if not resolved.is_file() or resolved.suffix.lower() != ".json":
        raise SocialVideoError("El plan debe ser un archivo JSON regular.")
    if {part.lower() for part in resolved.parts} & SENSITIVE_PARTS:
        raise SocialVideoError("El plan pertenece a una zona sensible.")
    return resolved


def classify_video(duration: float, size_bytes: int) -> str:
    if duration <= 0:
        raise SocialVideoError("No se pudo determinar una duracion valida.")
    if duration <= SHORT_MAX_SECONDS:
        if size_bytes > SHORT_MAX_BYTES:
            raise SocialVideoError("El video corto supera el limite de 100 MB.")
        return "short"
    if duration <= LONG_MAX_SECONDS:
        if size_bytes > LONG_MAX_BYTES:
            raise SocialVideoError("El video largo supera el limite de 1 GB.")
        return "long"
    raise SocialVideoError("El video supera el limite de 15 minutos.")


def check_disk_space(root: Path, size_bytes: int) -> None:
    probe = root
    while not probe.exists() and probe != probe.parent:
        probe = probe.parent
    free_bytes = shutil.disk_usage(probe).free
    required = size_bytes * 3 + RESERVED_DISK_BYTES
    if free_bytes < required:
        raise SocialVideoError("No hay espacio libre suficiente para conservar original y derivados.")


def job_path(data_root: Path, job_id: str) -> Path:
    if not re.fullmatch(r"video-[0-9]{8}T[0-9]{6}Z-[0-9a-f]{8}", job_id):
        raise SocialVideoError("Identificador de trabajo no valido.")
    root = validate_data_root(data_root)
    candidate = (root / job_id).resolve()
    if candidate.parent != root:
        raise SocialVideoError("El trabajo debe permanecer dentro del almacen privado.")
    return candidate


def state_path(job_dir: Path) -> Path:
    return job_dir / "state.json"


def load_state(job_dir: Path) -> dict[str, Any]:
    if not job_dir.is_dir():
        raise SocialVideoError("No existe el trabajo solicitado.")
    state = read_json(state_path(job_dir))
    if state.get("status") not in VALID_STATES:
        raise SocialVideoError("El trabajo contiene un estado no valido.")
    return state


def append_event(state: dict[str, Any], status: str, detail: str) -> None:
    if status not in VALID_STATES:
        raise SocialVideoError("Transicion a estado no valido.")
    now = iso_now()
    state["status"] = status
    state["updated_at"] = now
    state.setdefault("history", []).append({"at": now, "status": status, "detail": detail})


def ingest_video(video_path: Path, data_root: Path) -> dict[str, Any]:
    source = validate_source_path(video_path)
    root = validate_data_root(data_root)
    private_directory(root, exist_ok=True)

    probe = PREPARER.probe_video(source)
    metadata = PREPARER.summarize_probe(probe, source.stat().st_size)
    if not metadata.get("width") or not metadata.get("height"):
        raise SocialVideoError("No se encontro una pista de video valida.")
    mode = classify_video(float(metadata["duration_seconds"]), source.stat().st_size)
    check_disk_space(root, source.stat().st_size)

    job_id = f"video-{utc_now().strftime('%Y%m%dT%H%M%SZ')}-{uuid.uuid4().hex[:8]}"
    job_dir = job_path(root, job_id)
    private_directory(job_dir)
    for name in ("source", "analysis", "plans", "previews", "exports"):
        private_directory(job_dir / name)

    original = job_dir / "source" / f"original{source.suffix.lower()}"
    source_checksum = sha256_file(source)
    shutil.copyfile(source, original)
    os.chmod(original, 0o400 if os.name != "nt" else 0o600)
    copied_checksum = sha256_file(original)
    if source_checksum != copied_checksum:
        raise SocialVideoError("El checksum del original copiado no coincide.")

    created = iso_now()
    state = {
        "schema_version": 1,
        "job_id": job_id,
        "status": "received",
        "mode": mode,
        "created_at": created,
        "updated_at": created,
        "source": {
            "original_path": str(original),
            "original_name": source.name,
            "sha256": copied_checksum,
            "size_bytes": source.stat().st_size,
        },
        "metadata": metadata,
        "current_revision": 0,
        "selected_variant": None,
        "history": [{"at": created, "status": "received", "detail": "Original privado copiado y verificado."}],
    }
    write_private_json(state_path(job_dir), state)
    return public_state(state, job_dir)


def create_contact_sheet(video: Path, output: Path, duration: float, mode: str) -> None:
    if not shutil.which("ffmpeg"):
        raise SocialVideoError("ffmpeg no esta disponible.")
    samples = 9 if mode == "short" else 16
    columns = 3 if mode == "short" else 4
    rows = 3 if mode == "short" else 4
    sample_rate = samples / max(duration, 1.0)
    video_filter = (
        f"fps={sample_rate:.8f},scale=360:-2:flags=lanczos,"
        f"tile={columns}x{rows}:padding=6:margin=6:color=black"
    )
    PREPARER.run_command(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(video),
            "-vf",
            video_filter,
            "-frames:v",
            "1",
            str(output),
        ]
    )
    os.chmod(output, 0o600)


def detect_scene_changes(video: Path, threshold: float = 0.35) -> list[float]:
    if not shutil.which("ffmpeg"):
        raise SocialVideoError("ffmpeg no esta disponible.")
    completed = subprocess.run(
        [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "info",
            "-i",
            str(video),
            "-vf",
            f"select='gt(scene,{threshold})',showinfo",
            "-an",
            "-f",
            "null",
            "-",
        ],
        check=False,
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise SocialVideoError("No se pudieron detectar cambios de escena.")
    values: list[float] = []
    for match in SCENE_TIME_RE.finditer(completed.stderr):
        value = round(float(match.group(1)), 3)
        if not values or value - values[-1] >= 0.5:
            values.append(value)
        if len(values) == 60:
            break
    return values


def analyze_job(job_dir: Path, whisper_model: str, no_transcribe: bool) -> dict[str, Any]:
    state = load_state(job_dir)
    if state["status"] not in {"received", "failed"}:
        raise SocialVideoError("El trabajo ya fue analizado o no admite reanalisis.")
    original = Path(state["source"]["original_path"])
    if sha256_file(original) != state["source"]["sha256"]:
        raise SocialVideoError("El original cambio desde la ingesta.")

    analysis_dir = job_dir / "analysis"
    contact_sheet = analysis_dir / "contact-sheet.jpg"
    try:
        create_contact_sheet(
            original,
            contact_sheet,
            float(state["metadata"]["duration_seconds"]),
            state["mode"],
        )
        transcription: dict[str, Any] = {"status": "skipped", "segments": [], "text": ""}
        warnings: list[str] = []
        if state["metadata"].get("audio_present") and not no_transcribe:
            try:
                transcription = PREPARER.transcribe_video(original, whisper_model)
                transcription["status"] = "completed"
            except Exception as exc:  # Visual analysis still provides a useful fallback.
                warnings.append(f"Transcripcion no disponible: {type(exc).__name__}")
                transcription = {"status": "failed", "segments": [], "text": ""}
        scene_changes: list[float] = []
        if state["mode"] == "long":
            scene_changes = detect_scene_changes(original)
        analysis = {
            "schema_version": 1,
            "job_id": state["job_id"],
            "mode": state["mode"],
            "metadata": state["metadata"],
            "contact_sheet": str(contact_sheet),
            "transcription": transcription,
            "scene_changes_seconds": scene_changes,
            "warnings": warnings,
            "sharing_boundary": "Solo transcripcion y hojas de fotogramas pueden enviarse al modelo configurado.",
        }
        write_private_json(analysis_dir / "analysis.json", analysis)
        append_event(state, "analyzed", "Fotogramas y audio analizados localmente.")
        write_private_json(state_path(job_dir), state)
        return {
            **public_state(state, job_dir),
            "contact_sheet": str(contact_sheet),
            "analysis_file": str(analysis_dir / "analysis.json"),
            "transcript_segments": len(transcription.get("segments", [])),
            "scene_changes": len(scene_changes),
            "warnings": warnings,
        }
    except Exception as exc:
        append_event(state, "failed", f"Analisis fallido: {type(exc).__name__}")
        write_private_json(state_path(job_dir), state)
        raise


def number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise SocialVideoError(f"{field} debe ser numerico.")
    return float(value)


def validate_overlay(value: Any, clip_duration: float) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise SocialVideoError("Cada texto debe ser un objeto.")
    text = value.get("text")
    if not isinstance(text, str) or not text.strip() or len(text.strip()) > MAX_OVERLAY_CHARS:
        raise SocialVideoError("Cada texto debe tener entre 1 y 120 caracteres.")
    start = number(value.get("start"), "overlay.start")
    end = number(value.get("end"), "overlay.end")
    if start < 0 or end <= start or end > clip_duration:
        raise SocialVideoError("Los tiempos del texto quedan fuera del clip.")
    position = value.get("position", "top")
    if position not in {"top", "center", "bottom"}:
        raise SocialVideoError("La posicion del texto no es valida.")
    return {"text": text.strip(), "start": start, "end": end, "position": position}


def validate_plan(plan: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    if plan.get("publish") not in {None, False}:
        raise SocialVideoError("El plan no puede publicar ni programar contenido.")
    selected = plan.get("selected_moment")
    if not isinstance(selected, dict):
        raise SocialVideoError("El plan debe justificar un momento seleccionado.")
    selected_start = number(selected.get("start"), "selected_moment.start")
    selected_end = number(selected.get("end"), "selected_moment.end")
    reason = selected.get("reason")
    source_duration = float(state["metadata"]["duration_seconds"])
    if not isinstance(reason, str) or len(reason.strip()) < 8:
        raise SocialVideoError("El momento seleccionado necesita una razon narrativa concreta.")
    if selected_start < 0 or selected_end <= selected_start or selected_end > source_duration + 0.01:
        raise SocialVideoError("El momento seleccionado queda fuera del video original.")
    if selected_end - selected_start > MAX_OUTPUT_SECONDS:
        raise SocialVideoError("El momento seleccionado supera 60 segundos.")

    variants = plan.get("variants")
    if not isinstance(variants, dict) or set(variants) != set(VARIANT_KEYS):
        raise SocialVideoError("El plan debe contener exactamente las variantes A, B y C.")
    cleaned_variants: dict[str, Any] = {}
    for key in VARIANT_KEYS:
        raw = variants[key]
        if not isinstance(raw, dict):
            raise SocialVideoError(f"La variante {key} debe ser un objeto.")
        start = number(raw.get("start", selected_start), f"variants.{key}.start")
        end = number(raw.get("end", selected_end), f"variants.{key}.end")
        if start < selected_start or end > selected_end or end <= start:
            raise SocialVideoError(f"La variante {key} debe quedar dentro del momento seleccionado.")
        clip_duration = end - start
        freeze_end = number(raw.get("freeze_end", 0.0), f"variants.{key}.freeze_end")
        if freeze_end < 0 or freeze_end > 2.0 or clip_duration + freeze_end > MAX_OUTPUT_SECONDS:
            raise SocialVideoError(f"La duracion final de la variante {key} no es valida.")
        if clip_duration < MIN_OUTPUT_SECONDS:
            raise SocialVideoError(f"La variante {key} es demasiado corta.")
        zoom = number(raw.get("zoom", 1.0), f"variants.{key}.zoom")
        if not MIN_ZOOM <= zoom <= MAX_ZOOM:
            raise SocialVideoError(f"El zoom de la variante {key} debe estar entre 1.00 y 1.35.")
        framing = raw.get("framing", "fit")
        if framing not in {"fit", "crop-center"}:
            raise SocialVideoError(f"El encuadre de la variante {key} no es valido.")
        overlays = raw.get("overlays", [])
        if not isinstance(overlays, list) or len(overlays) > MAX_OVERLAYS:
            raise SocialVideoError(f"La variante {key} admite como maximo tres textos.")
        cleaned_variants[key] = {
            "label": str(raw.get("label", key)).strip() or key,
            "start": start,
            "end": end,
            "zoom": zoom,
            "framing": framing,
            "subtitles": bool(raw.get("subtitles", True)),
            "freeze_end": freeze_end,
            "overlays": [validate_overlay(item, clip_duration + freeze_end) for item in overlays],
        }

    return {
        "schema_version": 1,
        "job_id": state["job_id"],
        "selected_moment": {
            "start": selected_start,
            "end": selected_end,
            "reason": reason.strip(),
        },
        "variants": cleaned_variants,
        "recommendation": str(plan.get("recommendation", "")).strip(),
        "hook": str(plan.get("hook", "")).strip(),
        "caption": str(plan.get("caption", "")).strip(),
        "platform": str(plan.get("platform", "TikTok, Reels y Shorts")).strip(),
        "privacy": plan.get("privacy", []),
        "publish": False,
    }


def ass_time(seconds: float) -> str:
    centiseconds = max(0, round(seconds * 100))
    hours, remainder = divmod(centiseconds, 360000)
    minutes, remainder = divmod(remainder, 6000)
    whole_seconds, centis = divmod(remainder, 100)
    return f"{hours}:{minutes:02d}:{whole_seconds:02d}.{centis:02d}"


def ass_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("{", "\\{").replace("}", "\\}").replace("\n", "\\N")


def transcript_events(analysis: dict[str, Any], start: float, end: float) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for segment in analysis.get("transcription", {}).get("segments", []):
        try:
            seg_start = float(segment["start"])
            seg_end = float(segment["end"])
            text = str(segment["text"]).strip()
        except (KeyError, TypeError, ValueError):
            continue
        if text and seg_end > start and seg_start < end:
            events.append(
                {
                    "start": max(seg_start, start) - start,
                    "end": min(seg_end, end) - start,
                    "text": text,
                    "style": "Subtitle",
                }
            )
    return events


def write_ass_file(path: Path, events: list[dict[str, Any]], width: int, height: int) -> None:
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {width}
PlayResY: {height}
WrapStyle: 2

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Subtitle,Arial,52,&H00FFFFFF,&H000000FF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,2,70,70,100,1
Style: Top,Arial,58,&H00FFFFFF,&H000000FF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,8,70,70,95,1
Style: Center,Arial,58,&H00FFFFFF,&H000000FF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,5,70,70,70,1
Style: Bottom,Arial,58,&H00FFFFFF,&H000000FF,&H00101010,&H90000000,-1,0,0,0,100,100,0,0,1,3,1,2,70,70,100,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [header]
    for event in events:
        lines.append(
            "Dialogue: 0,"
            f"{ass_time(float(event['start']))},{ass_time(float(event['end']))},"
            f"{event['style']},,0,0,0,,{ass_escape(str(event['text']))}\n"
        )
    path.write_text("".join(lines), encoding="utf-8", newline="\n")
    os.chmod(path, 0o600)


def target_resolution(metadata: dict[str, Any]) -> tuple[int, int]:
    width = int(metadata.get("width") or 0)
    height = int(metadata.get("height") or 0)
    if min(width, height) >= 1080 and max(width, height) >= 1920:
        return 1080, 1920
    return 720, 1280


def filter_path(path: Path) -> str:
    return str(path).replace("\\", "/").replace(":", "\\:").replace("'", "\\'")


def build_ffmpeg_command(
    source: Path,
    output: Path,
    ass_file: Path | None,
    variant: dict[str, Any],
    metadata: dict[str, Any],
) -> list[str]:
    width, height = target_resolution(metadata)
    if variant["framing"] == "crop-center":
        filters = [
            f"scale={width}:{height}:force_original_aspect_ratio=increase",
            f"crop={width}:{height}",
        ]
    else:
        filters = [
            f"scale={width}:{height}:force_original_aspect_ratio=decrease",
            f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=black",
        ]
    zoom = float(variant["zoom"])
    if zoom > 1.0001:
        scaled_width = int(round(width * zoom / 2) * 2)
        scaled_height = int(round(height * zoom / 2) * 2)
        filters.extend([f"scale={scaled_width}:{scaled_height}", f"crop={width}:{height}"])
    if ass_file is not None:
        filters.append(f"ass='{filter_path(ass_file)}'")
    freeze_end = float(variant["freeze_end"])
    if freeze_end:
        filters.append(f"tpad=stop_mode=clone:stop_duration={freeze_end:.3f}")

    clip_duration = float(variant["end"]) - float(variant["start"])
    command = [
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-ss",
        f"{float(variant['start']):.3f}",
        "-t",
        f"{clip_duration:.3f}",
        "-i",
        str(source),
        "-map",
        "0:v:0",
        "-map",
        "0:a?",
        "-vf",
        ",".join(filters),
    ]
    if metadata.get("audio_present"):
        command.extend(["-af", "loudnorm=I=-16:LRA=11:TP=-1.5", "-c:a", "aac", "-b:a", "128k"])
    command.extend(
        [
            "-c:v",
            "libx264",
            "-preset",
            "veryfast",
            "-crf",
            "23",
            "-pix_fmt",
            "yuv420p",
            "-movflags",
            "+faststart",
            str(output),
        ]
    )
    return command


def render_variant(
    source: Path,
    output: Path,
    ass_file: Path | None,
    variant: dict[str, Any],
    metadata: dict[str, Any],
) -> None:
    if not shutil.which("ffmpeg"):
        raise SocialVideoError("ffmpeg no esta disponible.")
    command = build_ffmpeg_command(source, output, ass_file, variant, metadata)
    subprocess.run(command, check=True, capture_output=True, text=True)
    os.chmod(output, 0o600)


def verify_rendered_output(path: Path, expected_max_duration: float) -> dict[str, Any]:
    probe = PREPARER.probe_video(path)
    metadata = PREPARER.summarize_probe(probe, path.stat().st_size)
    duration = float(metadata["duration_seconds"])
    if duration <= 0 or duration > min(MAX_OUTPUT_SECONDS, expected_max_duration + 0.25):
        raise SocialVideoError("La duracion real del render no coincide con el plan.")
    if int(metadata.get("width") or 0) <= 0 or int(metadata.get("height") or 0) <= 0:
        raise SocialVideoError("El render no contiene una pista de video valida.")
    return metadata


def render_job(job_dir: Path, plan_file: Path) -> dict[str, Any]:
    state = load_state(job_dir)
    if state["status"] not in {"analyzed", "moment_selected", "rendered", "failed"}:
        raise SocialVideoError("El trabajo debe estar analizado antes de renderizar.")
    source = Path(state["source"]["original_path"])
    if sha256_file(source) != state["source"]["sha256"]:
        raise SocialVideoError("El original cambio desde la ingesta.")
    analysis = read_json(job_dir / "analysis" / "analysis.json")
    plan = validate_plan(read_json(validate_plan_file(plan_file)), state)
    revision = int(state.get("current_revision", 0)) + 1
    revision_name = f"r{revision:03d}"
    preview_dir = job_dir / "previews" / revision_name
    private_directory(preview_dir)
    stored_plan = job_dir / "plans" / f"{revision_name}.json"
    write_private_json(stored_plan, plan)

    width, height = target_resolution(state["metadata"])
    outputs: dict[str, Any] = {}
    try:
        if state["mode"] == "long":
            append_event(state, "moment_selected", "Momento narrativo seleccionado y justificado.")
        for key in VARIANT_KEYS:
            variant = plan["variants"][key]
            events: list[dict[str, Any]] = []
            if variant["subtitles"]:
                events.extend(transcript_events(analysis, variant["start"], variant["end"]))
            for overlay in variant["overlays"]:
                events.append(
                    {
                        "start": overlay["start"],
                        "end": overlay["end"],
                        "text": overlay["text"],
                        "style": overlay["position"].title(),
                    }
                )
            ass_file: Path | None = None
            if events:
                ass_file = preview_dir / f"{key}.ass"
                write_ass_file(ass_file, events, width, height)
            output = preview_dir / f"{key}.mp4"
            render_variant(source, output, ass_file, variant, state["metadata"])
            expected_duration = variant["end"] - variant["start"] + variant["freeze_end"]
            rendered_metadata = verify_rendered_output(output, expected_duration)
            outputs[key] = {
                "path": str(output),
                "sha256": sha256_file(output),
                "duration_seconds": rendered_metadata["duration_seconds"],
                "resolution": f"{rendered_metadata['width']}x{rendered_metadata['height']}",
                "label": variant["label"],
            }
        state["current_revision"] = revision
        state.setdefault("revisions", {})[revision_name] = {
            "plan_file": str(stored_plan),
            "outputs": outputs,
        }
        append_event(state, "rendered", f"Variantes A/B/C generadas en {revision_name}.")
        write_private_json(state_path(job_dir), state)
        return {**public_state(state, job_dir), "revision": revision_name, "outputs": outputs, "plan_file": str(stored_plan)}
    except Exception as exc:
        append_event(state, "failed", f"Render fallido: {type(exc).__name__}")
        write_private_json(state_path(job_dir), state)
        raise


def approve_job(job_dir: Path, variant: str, revision: str | None = None) -> dict[str, Any]:
    state = load_state(job_dir)
    if state["status"] != "rendered":
        raise SocialVideoError("Solo se puede aprobar un trabajo renderizado.")
    key = variant.upper()
    if key not in VARIANT_KEYS:
        raise SocialVideoError("La variante debe ser A, B o C.")
    revision_name = revision or f"r{int(state['current_revision']):03d}"
    revision_data = state.get("revisions", {}).get(revision_name)
    if not isinstance(revision_data, dict):
        raise SocialVideoError("No existe la revision solicitada.")
    output_data = revision_data.get("outputs", {}).get(key)
    if not isinstance(output_data, dict):
        raise SocialVideoError("No existe la variante solicitada.")
    preview = Path(output_data["path"])
    if sha256_file(preview) != output_data["sha256"]:
        raise SocialVideoError("La preview cambio desde su renderizado.")

    append_event(state, "approved", f"Variante {key} de {revision_name} aprobada por el usuario.")
    export = job_dir / "exports" / f"{state['job_id']}-{key}-{revision_name}.mp4"
    shutil.copyfile(preview, export)
    os.chmod(export, 0o600)
    export_checksum = sha256_file(export)
    if export_checksum != output_data["sha256"]:
        raise SocialVideoError("El archivo exportado no coincide con la preview aprobada.")
    state["selected_variant"] = {"variant": key, "revision": revision_name}
    state["export"] = {"path": str(export), "sha256": export_checksum}
    append_event(state, "exported", "Version aprobada exportada; no se publico nada.")
    write_private_json(state_path(job_dir), state)
    return {
        **public_state(state, job_dir),
        "selected_variant": state["selected_variant"],
        "export": state["export"],
        "published": False,
    }


def discard_job(job_dir: Path) -> dict[str, Any]:
    state = load_state(job_dir)
    if state["status"] == "exported":
        raise SocialVideoError("Un trabajo exportado no se descarta automaticamente.")
    append_event(state, "discarded", "Trabajo descartado por el usuario; no se borro ningun archivo.")
    write_private_json(state_path(job_dir), state)
    return public_state(state, job_dir)


def public_state(state: dict[str, Any], job_dir: Path) -> dict[str, Any]:
    return {
        "ok": True,
        "job_id": state["job_id"],
        "status": state["status"],
        "mode": state["mode"],
        "created_at": state["created_at"],
        "updated_at": state["updated_at"],
        "job_dir": str(job_dir),
        "duration_seconds": state["metadata"]["duration_seconds"],
        "resolution": f"{state['metadata']['width']}x{state['metadata']['height']}",
        "current_revision": state.get("current_revision", 0),
    }


def list_states(data_root: Path) -> list[tuple[Path, dict[str, Any]]]:
    root = validate_data_root(data_root)
    if not root.is_dir():
        return []
    states: list[tuple[Path, dict[str, Any]]] = []
    for path in root.glob("video-*/state.json"):
        try:
            state = read_json(path)
            if state.get("status") in VALID_STATES:
                states.append((path.parent, state))
        except SocialVideoError:
            continue
    return sorted(states, key=lambda item: item[1].get("updated_at", ""), reverse=True)


def status_result(data_root: Path, requested_job_id: str | None) -> dict[str, Any]:
    if requested_job_id:
        directory = job_path(data_root, requested_job_id)
        return {**public_state(load_state(directory), directory), "active_jobs": None}
    states = list_states(data_root)
    if not states:
        raise SocialVideoError("No hay trabajos de video social.")
    active = [item for item in states if item[1]["status"] in ACTIVE_STATES]
    selected = active[0] if active else states[0]
    return {**public_state(selected[1], selected[0]), "active_jobs": len(active)}


def retention_report(data_root: Path, now: datetime) -> dict[str, Any]:
    candidates: list[dict[str, Any]] = []
    for _, state in list_states(data_root):
        days = RETENTION_DAYS.get(state["status"])
        if days is None:
            continue
        try:
            updated = datetime.fromisoformat(str(state["updated_at"]).replace("Z", "+00:00"))
            if updated.tzinfo is None:
                updated = updated.replace(tzinfo=timezone.utc)
        except ValueError:
            continue
        age = now - updated
        if age >= timedelta(days=days):
            candidates.append(
                {
                    "job_id": state["job_id"],
                    "status": state["status"],
                    "age_days": age.days,
                    "retention_days": days,
                }
            )
    return {
        "ok": True,
        "mode": "dry-run",
        "candidate_count": len(candidates),
        "candidates": candidates,
        "changed": False,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Gestiona trabajos privados de video social.")
    parser.add_argument("--data-root", type=Path, default=DEFAULT_DATA_ROOT)
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest = subparsers.add_parser("ingest", help="Copia y verifica un original privado.")
    ingest.add_argument("video", type=Path)

    analyze = subparsers.add_parser("analyze", help="Genera fotogramas y transcripcion local.")
    analyze.add_argument("job_id")
    analyze.add_argument("--whisper-model", default="base")
    analyze.add_argument("--no-transcribe", action="store_true")

    render = subparsers.add_parser("render", help="Renderiza las variantes A/B/C de un plan.")
    render.add_argument("job_id")
    render.add_argument("--plan", type=Path, required=True)

    approve = subparsers.add_parser("approve", help="Aprueba y exporta una variante.")
    approve.add_argument("job_id")
    approve.add_argument("variant")
    approve.add_argument("--revision")

    status = subparsers.add_parser("status", help="Muestra el ultimo trabajo activo.")
    status.add_argument("job_id", nargs="?")

    discard = subparsers.add_parser("discard", help="Marca un trabajo como descartado sin borrarlo.")
    discard.add_argument("job_id")

    retention = subparsers.add_parser("retention", help="Lista candidatos antiguos sin borrar.")
    retention.add_argument("--dry-run", action="store_true", required=True)
    retention.add_argument("--now", help="Fecha ISO-8601 para pruebas repetibles.")
    return parser


def parse_now(value: str | None) -> datetime:
    if not value:
        return utc_now()
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    data_root = args.data_root
    try:
        if args.command == "ingest":
            result = ingest_video(args.video, data_root)
        elif args.command == "analyze":
            result = analyze_job(job_path(data_root, args.job_id), args.whisper_model, args.no_transcribe)
        elif args.command == "render":
            result = render_job(job_path(data_root, args.job_id), args.plan)
        elif args.command == "approve":
            result = approve_job(job_path(data_root, args.job_id), args.variant, args.revision)
        elif args.command == "status":
            result = status_result(data_root, args.job_id)
        elif args.command == "discard":
            result = discard_job(job_path(data_root, args.job_id))
        elif args.command == "retention":
            result = retention_report(data_root, parse_now(args.now))
        else:  # pragma: no cover - argparse prevents this path.
            raise SocialVideoError("Operacion no reconocida.")
    except (SocialVideoError, FileNotFoundError, subprocess.CalledProcessError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
