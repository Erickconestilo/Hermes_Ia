#!/usr/bin/env python3
"""Minimal private capture store for CiudadanoInusual mobile notes."""

from __future__ import annotations

import argparse
from datetime import datetime
import json
import os
from pathlib import Path
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
    path.write_text(content, encoding="utf-8")
    try:
        path.chmod(0o600)
    except OSError:
        pass


def parse_csv(value: str) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def validate_original_text(text: str) -> None:
    normalized_text = text.casefold()
    if any(marker.casefold() in normalized_text for marker in TEMPLATE_TEXT_MARKERS):
        raise SystemExit(TEMPLATE_TEXT_ERROR)


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
    print(json.dumps(capture, ensure_ascii=False, sort_keys=True))
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    records = read_records(store_path())
    if args.status:
        records = [record for record in records if record.get("status") == args.status]
    for record in records[-args.limit :]:
        preview = record.get("original_text", "").replace("\n", " ")[:90]
        print(f"{record['id']}\t{record['created_at']}\t{record['status']}\t{record.get('suggested_format','')}\t{preview}")
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
    print(json.dumps(record, ensure_ascii=False, sort_keys=True))
    return 0


def cmd_export_curated(args: argparse.Namespace) -> int:
    statuses = set(parse_csv(args.statuses))
    records = [record for record in read_records(store_path()) if record.get("status") in statuses]
    output = Path(args.output).expanduser()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records),
        encoding="utf-8",
    )
    print(json.dumps({"ok": True, "count": len(records), "output": str(output)}, ensure_ascii=False))
    return 0


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
    add.set_defaults(func=cmd_add)

    list_cmd = subparsers.add_parser("list", help="List recent captures.")
    list_cmd.add_argument("--status", choices=sorted(VALID_STATUSES))
    list_cmd.add_argument("--limit", type=int, default=20)
    list_cmd.set_defaults(func=cmd_list)

    show = subparsers.add_parser("show", help="Show one capture by id or id prefix.")
    show.add_argument("capture_id")
    show.set_defaults(func=cmd_show)

    update = subparsers.add_parser("update-status", help="Update status without modifying original_text.")
    update.add_argument("capture_id")
    update.add_argument("status", choices=sorted(VALID_STATUSES))
    update.add_argument("--derived-reference", default="")
    update.set_defaults(func=cmd_update_status)

    export = subparsers.add_parser("export-curated", help="Export reviewed/converted captures to a chosen file.")
    export.add_argument("--output", required=True)
    export.add_argument("--statuses", default="reviewed,converted")
    export.set_defaults(func=cmd_export_curated)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
