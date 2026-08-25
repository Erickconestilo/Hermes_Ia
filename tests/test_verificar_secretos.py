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

    def run_checker(self, files: dict[str, bytes | str]) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as tmpdir:
            workspace = Path(tmpdir)
            subprocess.run(["git", "init", "-q"], cwd=workspace, check=True)
            for name, content in files.items():
                path = workspace / name
                path.parent.mkdir(parents=True, exist_ok=True)
                if isinstance(content, bytes):
                    path.write_bytes(content)
                else:
                    path.write_text(content, encoding="utf-8")
            subprocess.run(["git", "add", "--all"], cwd=workspace, check=True)
            return subprocess.run(
                ["bash", str(SCRIPT)],
                cwd=workspace,
                text=True,
                capture_output=True,
                check=False,
                env={**os.environ, "LC_ALL": "C"},
            )

    def test_handles_non_ascii_staged_filename(self) -> None:
        secret = "ghp_" + "A" * 36
        result = self.run_checker({"archivo-ñ.txt": f"token={secret}\n"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("linea=1", result.stdout)
        self.assertNotIn(secret, result.stdout + result.stderr)

    def test_scans_binary_staged_file_as_text(self) -> None:
        secret = "sk-" + "B" * 36
        result = self.run_checker({"binario.dat": b"\x00" + secret.encode() + b"\x00"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("archivo=binario.dat", result.stdout)
        self.assertNotIn(secret, result.stdout + result.stderr)

    def test_flags_real_ip_even_when_same_line_contains_allowed_ip(self) -> None:
        real_ip = "203.0.113." + "77"
        result = self.run_checker({"network.txt": "proxy 127.0.0.1 -> vps " + real_ip + "\n"})
        self.assertEqual(result.returncode, 1)
        self.assertIn("archivo=network.txt linea=1", result.stdout)

    def test_detects_github_private_key_and_aws_patterns_without_leaking_values(self) -> None:
        github = "gho_" + "C" * 36
        aws = "AKIA" + "D" * 16
        private_key = "-----BEGIN " + "OPENSSH PRIVATE KEY-----"
        result = self.run_checker({
            "secrets.txt": f"github={github}\naws={aws}\n{private_key}\n",
        })
        self.assertEqual(result.returncode, 1)
        self.assertGreaterEqual(result.stdout.count("archivo=secrets.txt"), 3)
        self.assertNotIn(github, result.stdout + result.stderr)
        self.assertNotIn(aws, result.stdout + result.stderr)
        self.assertNotIn(private_key, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
