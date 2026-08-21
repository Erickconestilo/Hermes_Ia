"""Regression tests for the staged-secret checker output."""

from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "verificar-secretos.sh"


class VerificarSecretosTests(unittest.TestCase):
    def test_reports_only_metadata_for_staged_secret_and_ip(self) -> None:
        # Compose fixtures so the repository scanner does not flag its own test.
        secret = "sk-" + "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        ip_address = "198.51." + "100.42"

        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            subprocess.run(["git", "init", "-q"], cwd=workspace, check=True)
            (workspace / "sample.txt").write_text(
                f"token={secret}\nhost={ip_address}\n", encoding="utf-8"
            )
            subprocess.run(["git", "add", "sample.txt"], cwd=workspace, check=True)

            result = subprocess.run(
                ["bash", str(SCRIPT)],
                cwd=workspace,
                text=True,
                capture_output=True,
                check=False,
                env={**os.environ, "LC_ALL": "C"},
            )

        self.assertEqual(result.returncode, 1)
        self.assertIn("archivo=sample.txt linea=1", result.stdout)
        self.assertIn("archivo=sample.txt linea=2", result.stdout)
        self.assertNotIn(secret, result.stdout)
        self.assertNotIn(ip_address, result.stdout)
        self.assertNotIn(secret, result.stderr)
        self.assertNotIn(ip_address, result.stderr)
