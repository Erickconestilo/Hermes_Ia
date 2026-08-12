#!/usr/bin/env python3
"""Minimal private capture store for CiudadanoInusual mobile notes."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
import tempfile
from typing import Any
from uuid import uuid4
from zoneinfo import ZoneInfo
from zoneinfo import ZoneInfoNotFoundError


DEFAULT_STORE = Path("/home/hermes/.hermes/data/ciudadanoinusual/capturas.jsonl")
VALID_INPUT_TYPES = {"text", "voice", "image_note"}
VALID_STATUSES = {"inbox", "reviewed", "converted", "discarded"}
TEMPLATE_TEXT_MARKERS = (
    "[cuenta aquí",
    "Antes de guardar:",
    "Devuélveme",
    "No lo conviertas",
    "Detecta riesgos",
    "Usa scripts/captura-movil.py",
    "No metas nada en Git",
)
TEMPLATE_TEXT_ERROR = "El texto parece incluir instrucciones o plantilla. Pasa solo la situación real."
POLICY_OVERRIDE_MARKERS = (
    "ignora tus reglas",
    "ignora las reglas",
    "ignore previous instructions",
    "ignore your rules",
    "modifica la política",
    "desactiva la seguridad",
    "envía el .env",
    "sube el .env",
)
POLICY_OVERRIDE_ERROR = "El texto intenta modificar la política operativa y fue rechazado."


class ExportPathError(ValueError):
    """Raised when an export target escapes the configured safe root."""


def madrid_now() -> datetime:
    try:
        return datetime.now(ZoneInfo("Europe/Madrid"))
    except ZoneInfoNotFoundError:
        # Windows Python installs may not include tzdata. The user's local
        # machine is configured for Europe/Madrid; VPS Linux should use ZoneInfo.
        return datetime.now().astimezone()


def store_path() -> Path:
    override = os.environ.get("HERMES_CAPTURE_STORE")
    return Path(override).expanduser() if override else DEFAULT_STORE


def export_root() -> Path:
    override = os.environ.get("HERMES_CAPTURE_EXPORT_ROOT")
    selected = Path(override).expanduser() if override else store_path().parent / "exports"
    return selected.resolve(strict=False)


def read_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSONL at {path}:{line_number}: {exc}") from exc
    return records


def write_records(path: Path, records: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    atomic_write_text(path, content, overwrite=True)


def atomic_write_text(path: Path, content: str, *, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    if not overwrite and path.exists():
        raise FileExistsError("destination already exists")
    file_descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary_path = Path(temporary_name)
    try:
        try:
            os.fchmod(file_descriptor, 0o600)
        except (AttributeError, OSError):
            pass
        with os.fdopen(file_descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        if overwrite:
            os.replace(temporary_path, path)
        else:
            os.link(temporary_path, path)
            temporary_path.unlink()
        try:
            path.chmod(0o600)
        except OSError:
            pass
    finally:
        try:
            temporary_path.unlink()
        except FileNotFoundError:
            pass


def _path_has_symlink(path: Path) -> bool:
    absolute = path if path.is_absolute() else Path.cwd() / path
    current = Path(absolute.anchor)
    for part in absolute.parts[1:]:
        current /= part
        if current.is_symlink():
            return True
    return False


def _is_sensitive_destination(path: Path) -> bool:
    lowered_parts = {part.casefold() for part in path.parts}
    name = path.name.casefold()
    return (
        ".ssh" in lowered_parts
        or name == ".env"
        or name.startswith(".env.")
        or name in {
            "authorized_keys",
            "id_rsa",
            "id_ed25519",
            "credentials",
            "config.yaml",
        }
    )


def resolve_export_output(raw_output: str) -> Path:
    requested = Path(raw_output).expanduser()
    if ".." in requested.parts:
        raise ExportPathError("parent traversal is not allowed")
    root = export_root()
    candidate = requested if requested.is_absolute() else root / requested
    if _path_has_symlink(candidate):
        raise ExportPathError("symbolic links are not allowed")
    resolved = candidate.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ExportPathError("destination is outside the export root") from exc
    if _is_sensitive_destination(resolved):
        raise ExportPathError("sensitive destinations are not allowed")
    return resolved


def parse_csv(value: str) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def validate_original_text(text: str) -> None:
    normalized_text = text.casefold()
    if any(marker.casefold() in normalized_text for marker in TEMPLATE_TEXT_MARKERS):
        raise SystemExit(TEMPLATE_TEXT_ERROR)
    if any(marker.casefold() in normalized_text for marker in POLICY_OVERRIDE_MARKERS):
        raise SystemExit(POLICY_OVERRIDE_ERROR)


def output_record(record: dict[str, Any], *, include_body: bool = False) -> dict[str, Any]:
    hidden = {"original_text", "transcript"}
    if include_body:
        return dict(record)
    return {key: value for key, value in record.items() if key not in hidden}


def find_record(records: list[dict[str, Any]], capture_id: str) -> dict[str, Any]:
    matches = [record for record in records if record["id"].startswith(capture_id)]
    if not matches:
        raise SystemExit(f"Capture not found: {capture_id}")
    if len(matches) > 1:
        raise SystemExit(f"Capture id is ambiguous: {capture_id}")
    return matches[0]


def cmd_add(args: argparse.Namespace) -> int:
    if args.input_type not in VALID_INPUT_TYPES:
        raise SystemExit(f"Invalid input_type. Use one of: {', '.join(sorted(VALID_INPUT_TYPES))}")
    validate_original_text(args.text)

    path = store_path()
    records = read_records(path)
    current_time = madrid_now()
    now = current_time.isoformat(timespec="seconds")
    capture = {
        "id": f"cap-{current_time.strftime('%Y%m%d%H%M%S')}-{uuid4().hex[:8]}",
        "created_at": now,
        "source": args.source,
        "input_type": args.input_type,
        "original_text": args.text,
        "transcript": args.transcript or "",
        "tags": parse_csv(args.tags),
        "privacy_flags": parse_csv(args.privacy_flags),
        "suggested_format": args.suggested_format or "",
        "status": "inbox",
        "derived_reference": "",
    }
    records.append(capture)
    write_records(path, records)
    print(json.dumps(output_record(capture, include_body=args.include_body), ensure_ascii=False, sort_keys=True))
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    records = read_records(store_path())
    if args.status:
        records = [record for record in records if record.get("status") == args.status]
    selected = [] if args.limit == 0 else records[-args.limit :]
    for record in selected:
        fields = [
            record["id"],
            record["created_at"],
            record["status"],
            record.get("suggested_format", ""),
        ]
        if args.include_preview:
            fields.append(record.get("original_text", "").replace("\n", " ")[:90])
        print("\t".join(fields))
    return 0


def cmd_show(args: argparse.Namespace) -> int:
    record = find_record(read_records(store_path()), args.capture_id)
    print(json.dumps(record, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


def cmd_update_status(args: argparse.Namespace) -> int:
    if args.status not in VALID_STATUSES:
        raise SystemExit(f"Invalid status. Use one of: {', '.join(sorted(VALID_STATUSES))}")
    path = store_path()
    records = read_records(path)
    record = find_record(records, args.capture_id)
    record["status"] = args.status
    if args.derived_reference:
        record["derived_reference"] = args.derived_reference
    write_records(path, records)
    print(json.dumps(output_record(record, include_body=args.include_body), ensure_ascii=False, sort_keys=True))
    return 0


def cmd_export_curated(args: argparse.Namespace) -> int:
    statuses = set(parse_csv(args.statuses))
    records = [record for record in read_records(store_path()) if record.get("status") in statuses]
    try:
        output = resolve_export_output(args.output)
        atomic_write_text(
            output,
            "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
            overwrite=args.overwrite,
        )
    except ExportPathError as exc:
        raise SystemExit(f"Export rejected: {exc}") from exc
    except FileExistsError as exc:
        raise SystemExit("Export rejected: destination already exists. Use --overwrite explicitly.") from exc
    print(json.dumps({"ok": True, "count": len(records), "output": str(output)}, ensure_ascii=False))
    return 0


def nonnegative_int(value: str) -> int:
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("must be zero or greater")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Private mobile capture store for Hermes IA.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add = subparsers.add_parser("add", help="Add a new immutable capture.")
    add.add_argument("--text", required=True, help="Original raw text. This is immutable.")
    add.add_argument("--source", default="telegram")
    add.add_argument("--input-type", default="text")
    add.add_argument("--transcript", default="")
    add.add_argument("--tags", default="", help="Comma-separated tags.")
    add.add_argument("--privacy-flags", default="", help="Comma-separated privacy flags.")
    add.add_argument("--suggested-format", default="")
    add.add_argument("--include-body", action="store_true", help="Include private text in command output explicitly.")
    add.set_defaults(func=cmd_add)

    list_cmd = subparsers.add_parser("list", help="List recent captures.")
    list_cmd.add_argument("--status", choices=sorted(VALID_STATUSES))
    list_cmd.add_argument("--limit", type=nonnegative_int, default=20, help="0 returns no records; N returns at most N.")
    list_cmd.add_argument("--include-preview", action="store_true", help="Include a private text preview explicitly.")
    list_cmd.set_defaults(func=cmd_list)

    show = subparsers.add_parser("show", help="Show one capture by id or id prefix.")
    show.add_argument("capture_id")
    show.set_defaults(func=cmd_show)

    update = subparsers.add_parser("update-status", help="Update status without modifying original_text.")
    update.add_argument("capture_id")
    update.add_argument("status", choices=sorted(VALID_STATUSES))
    update.add_argument("--derived-reference", default="")
    update.add_argument("--include-body", action="store_true", help="Include private text in command output explicitly.")
    update.set_defaults(func=cmd_update_status)

    export = subparsers.add_parser("export-curated", help="Export reviewed/converted captures to a chosen file.")
    export.add_argument("--output", required=True)
    export.add_argument("--statuses", default="reviewed,converted")
    export.add_argument("--overwrite", action="store_true", help="Replace an existing export explicitly.")
    export.set_defaults(func=cmd_export_curated)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
