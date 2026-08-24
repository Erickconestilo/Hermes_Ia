#!/usr/bin/env python3
"""Prepare a private video for social-media review by Hermes."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPORTED_SUFFIXES = {".mp4", ".webm", ".mov", ".avi", ".mkv", ".mpeg", ".mpg"}
MAX_BYTES = 50 * 1024 * 1024
SENSITIVE_PARTS = {".ssh", ".gnupg", "secrets", "credentials"}


class VideoPreparationError(RuntimeError):
    """Raised when a video cannot be prepared safely."""


def validate_video(path: Path) -> Path:
    candidate = path.expanduser()
    if candidate.is_symlink():
        raise VideoPreparationError("La ruta no puede ser un enlace simbolico.")
    resolved = candidate.resolve(strict=True)
    if not resolved.is_file():
        raise VideoPreparationError("La ruta debe ser un archivo de video regular.")
    if resolved.suffix.lower() not in SUPPORTED_SUFFIXES:
        raise VideoPreparationError("Formato no admitido para analisis de video.")
    if resolved.stat().st_size > MAX_BYTES:
        raise VideoPreparationError("El video supera el limite de 50 MB.")
    lowered_parts = {part.lower() for part in resolved.parts}
    if lowered_parts & SENSITIVE_PARTS or resolved.name.lower().startswith(".env"):
        raise VideoPreparationError("La ruta del video pertenece a una zona sensible.")
    return resolved


def parse_fraction(value: str | None) -> float | None:
    if not value or value in {"0/0", "N/A"}:
        return None
    try:
        if "/" in value:
            numerator, denominator = value.split("/", 1)
            return float(numerator) / float(denominator)
        return float(value)
    except (ValueError, ZeroDivisionError):
        return None


def summarize_probe(probe: dict[str, Any], size_bytes: int) -> dict[str, Any]:
    streams = probe.get("streams", [])
    video = next((item for item in streams if item.get("codec_type") == "video"), {})
    audio = next((item for item in streams if item.get("codec_type") == "audio"), {})
    raw_duration = probe.get("format", {}).get("duration") or video.get("duration") or 0
    try:
        duration = max(float(raw_duration), 0.0)
    except (TypeError, ValueError):
        duration = 0.0
    return {
        "duration_seconds": round(duration, 3),
        "size_bytes": size_bytes,
        "width": int(video.get("width") or 0),
        "height": int(video.get("height") or 0),
        "fps": parse_fraction(video.get("avg_frame_rate")),
        "video_codec": video.get("codec_name") or "unknown",
        "audio_present": bool(audio),
        "audio_codec": audio.get("codec_name") if audio else None,
    }


def run_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, capture_output=True, text=True)


def probe_video(video: Path) -> dict[str, Any]:
    if not shutil.which("ffprobe"):
        raise VideoPreparationError("ffprobe no esta disponible.")
    completed = run_command(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_format",
            "-show_streams",
            "-of",
            "json",
            str(video),
        ]
    )
    return json.loads(completed.stdout)


def create_contact_sheet(video: Path, output: Path, duration: float) -> None:
    if not shutil.which("ffmpeg"):
        raise VideoPreparationError("ffmpeg no esta disponible.")
    sample_rate = 9.0 / max(duration, 1.0)
    video_filter = (
        f"fps={sample_rate:.6f},scale=480:-2:flags=lanczos,"
        "tile=3x3:padding=8:margin=8:color=black"
    )
    run_command(
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


def transcribe_video(video: Path, model_name: str) -> dict[str, Any]:
    try:
        from faster_whisper import WhisperModel
    except ImportError as exc:
        raise VideoPreparationError("faster-whisper no esta disponible.") from exc

    model = WhisperModel(model_name, device="cpu", compute_type="int8")
    segments, info = model.transcribe(str(video), vad_filter=True)
    items = []
    for segment in segments:
        text = segment.text.strip()
        if text:
            items.append(
                {
                    "start": round(float(segment.start), 2),
                    "end": round(float(segment.end), 2),
                    "text": text,
                }
            )
    return {
        "language": getattr(info, "language", None),
        "language_probability": round(float(getattr(info, "language_probability", 0.0)), 4),
        "segments": items,
        "text": " ".join(item["text"] for item in items),
    }


def private_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=False, mode=0o700)
    os.chmod(path, 0o700)


def write_private_json(path: Path, payload: dict[str, Any]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    os.chmod(path, 0o600)


def prepare_video(args: argparse.Namespace) -> dict[str, Any]:
    video = validate_video(Path(args.video))
    output_root = Path(args.output_root).expanduser().resolve()
    output_root.mkdir(parents=True, exist_ok=True, mode=0o700)
    os.chmod(output_root, 0o700)

    stamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    work_dir = output_root / f"video-{stamp}-{uuid.uuid4().hex[:8]}"
    private_directory(work_dir)

    probe = probe_video(video)
    metadata = summarize_probe(probe, video.stat().st_size)
    if not metadata["width"] or not metadata["height"]:
        raise VideoPreparationError("No se encontro una pista de video valida.")

    contact_sheet = work_dir / "contact-sheet.jpg"
    create_contact_sheet(video, contact_sheet, metadata["duration_seconds"])
    os.chmod(contact_sheet, 0o600)

    transcription: dict[str, Any] = {"status": "skipped", "segments": [], "text": ""}
    warnings: list[str] = []
    if metadata["audio_present"] and not args.no_transcribe:
        try:
            transcription = transcribe_video(video, args.whisper_model)
            transcription["status"] = "completed"
        except Exception as exc:  # Visual review remains useful if transcription fails.
            warnings.append(f"Transcripcion no disponible: {type(exc).__name__}")
            transcription = {"status": "failed", "segments": [], "text": ""}

    details_file = work_dir / "analysis-input.json"
    details = {
        "source_video": str(video),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "metadata": metadata,
        "transcription": transcription,
        "warnings": warnings,
    }
    write_private_json(details_file, details)

    return {
        "ok": True,
        "video_path": str(video),
        "work_dir": str(work_dir),
        "contact_sheet": str(contact_sheet),
        "details_file": str(details_file),
        "duration_seconds": metadata["duration_seconds"],
        "resolution": f"{metadata['width']}x{metadata['height']}",
        "audio_present": metadata["audio_present"],
        "transcript_segments": len(transcription.get("segments", [])),
        "warnings": warnings,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepara fotogramas y transcripcion privada para revisar un video social."
    )
    parser.add_argument("video", help="Ruta local del video recibido por Hermes.")
    parser.add_argument(
        "--output-root",
        default="/home/hermes/.hermes/cache/video-social",
        help="Directorio privado para resultados temporales.",
    )
    parser.add_argument(
        "--whisper-model",
        default="base",
        help="Modelo local de faster-whisper (por defecto: base).",
    )
    parser.add_argument("--no-transcribe", action="store_true", help="Omite la transcripcion.")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        result = prepare_video(args)
    except (VideoPreparationError, FileNotFoundError, subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
