#!/usr/bin/env python3
"""Review or explicitly purge expired private mobile captures."""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import tempfile
from typing import Any


DEFAULT_STORE = Path("/home/hermes/.hermes/data/ciudadanoinusual/capturas.jsonl")
RETENTION_DAYS = {
    "discarded": 30,
    "inbox": 90,
    "reviewed": 90,
    "converted": 180,
}


def parse_now(value: str | None) -> datetime:
    if not value:
        return datetime.now(timezone.utc)
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def read_records(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise SystemExit(f"Invalid JSONL at {path}:{line_number}") from exc
    return records


def created_at(record: dict[str, Any]) -> datetime | None:
    value = record.get("created_at")
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def expired_records(records: list[dict[str, Any]], now: datetime) -> tuple[list[dict[str, Any]], int]:
    expired: list[dict[str, Any]] = []
    invalid_dates = 0
    for record in records:
        status = record.get("status")
        days = RETENTION_DAYS.get(status)
        if days is None:
            continue
        timestamp = created_at(record)
        if timestamp is None:
            invalid_dates += 1
            continue
        if timestamp <= now - timedelta(days=days):
            expired.append(record)
    return expired, invalid_dates


def write_records(path: Path, records: list[dict[str, Any]]) -> None:
    content = "".join(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n" for record in records)
    descriptor, temporary_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(temporary_name)
    try:
        os.fchmod(descriptor, 0o600)
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
        path.chmod(0o600)
    finally:
        try:
            temporary.unlink()
        except FileNotFoundError:
            pass


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Review retention candidates without exposing capture bodies.")
    parser.add_argument("--store", type=Path, default=DEFAULT_STORE)
    parser.add_argument("--now", help="ISO-8601 reference time; useful for repeatable synthetic tests.")
    action = parser.add_mutually_exclusive_group()
    action.add_argument("--dry-run", action="store_true", help="Report candidates without changing the store.")
    action.add_argument("--apply", action="store_true", help="Remove candidates after an explicit approved review.")
    args = parser.parse_args(argv)

    path = args.store.expanduser()
    if not path.is_file():
        raise SystemExit(f"Capture store not found: {path}")
    records = read_records(path)
    candidates, invalid_dates = expired_records(records, parse_now(args.now))
    candidate_ids = {record.get("id", "<missing-id>") for record in candidates}

    if args.apply:
        write_records(path, [record for record in records if record.get("id") not in candidate_ids])

    print(
        json.dumps(
            {
                "mode": "apply" if args.apply else "dry-run",
                "total_records": len(records),
                "candidate_count": len(candidates),
                "candidate_ids": sorted(candidate_ids),
                "invalid_date_count": invalid_dates,
                "changed": bool(args.apply and candidates),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
