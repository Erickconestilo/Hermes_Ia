from __future__ import annotations

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("retencion_datos", REPO_ROOT / "scripts" / "retencion-datos.py")
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load retencion-datos.py")
retencion = importlib.util.module_from_spec(spec)
spec.loader.exec_module(retencion)


class RetentionDataTests(unittest.TestCase):
    def create_store(self, root: Path) -> Path:
        records = [
            {"id": "old-discarded", "created_at": "2026-01-01T00:00:00+00:00", "status": "discarded", "original_text": "synthetic private body"},
            {"id": "recent-inbox", "created_at": "2026-08-20T00:00:00+00:00", "status": "inbox", "original_text": "keep this synthetic body"},
            {"id": "old-converted", "created_at": "2026-01-01T00:00:00+00:00", "status": "converted", "original_text": "another synthetic body"},
        ]
        path = root / "capturas.jsonl"
        path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")
        return path

    def run_main(self, args: list[str]) -> tuple[int, dict[str, object]]:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = retencion.main(args)
        return code, json.loads(output.getvalue())

    def test_dry_run_reports_candidates_without_changing_synthetic_store(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = self.create_store(Path(temporary))
            before = path.read_text(encoding="utf-8")
            code, result = self.run_main(["--store", str(path), "--now", "2026-08-21T00:00:00+00:00", "--dry-run"])
            self.assertEqual(code, 0)
            self.assertEqual(result["mode"], "dry-run")
            self.assertEqual(result["candidate_count"], 2)
            self.assertEqual(result["candidate_ids"], ["old-converted", "old-discarded"])
            self.assertNotIn("synthetic private body", json.dumps(result))
            self.assertEqual(path.read_text(encoding="utf-8"), before)

    def test_apply_removes_only_expired_synthetic_records(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = self.create_store(Path(temporary))
            code, result = self.run_main(["--store", str(path), "--now", "2026-08-21T00:00:00+00:00", "--apply"])
            self.assertEqual(code, 0)
            self.assertTrue(result["changed"])
            remaining = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual([record["id"] for record in remaining], ["recent-inbox"])

    def test_apply_removes_expired_duplicate_and_missing_ids_by_record_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "capturas.jsonl"
            records = [
                {"id": "duplicate", "created_at": "2026-01-01T00:00:00+00:00", "status": "discarded"},
                {"id": "duplicate", "created_at": "2026-01-02T00:00:00+00:00", "status": "discarded"},
                {"created_at": "2026-01-03T00:00:00+00:00", "status": "discarded"},
                {"id": "keep", "created_at": "2026-08-20T00:00:00+00:00", "status": "inbox"},
            ]
            path.write_text("".join(json.dumps(record) + "\n" for record in records), encoding="utf-8")

            code, result = self.run_main([
                "--store", str(path), "--now", "2026-08-21T00:00:00+00:00", "--apply"
            ])

            self.assertEqual(code, 0)
            self.assertEqual(result["candidate_count"], 3)
            remaining = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            self.assertEqual(remaining, [{"id": "keep", "created_at": "2026-08-20T00:00:00+00:00", "status": "inbox"}])


if __name__ == "__main__":
    unittest.main()
