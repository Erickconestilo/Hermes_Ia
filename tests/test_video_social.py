import importlib.util
import json
import os
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "video-social.py"
SPEC = importlib.util.spec_from_file_location("video_social", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


def probe(duration=12.0, width=720, height=1280, audio=True):
    streams = [
        {
            "codec_type": "video",
            "codec_name": "h264",
            "width": width,
            "height": height,
            "avg_frame_rate": "30/1",
        }
    ]
    if audio:
        streams.append({"codec_type": "audio", "codec_name": "aac"})
    return {"format": {"duration": str(duration)}, "streams": streams}


def valid_plan(duration=12.0):
    return {
        "selected_moment": {
            "start": 0.0,
            "end": duration,
            "reason": "Contiene inicio, desarrollo y remate comprensible.",
        },
        "variants": {
            "A": {
                "label": "minima",
                "start": 0.0,
                "end": duration,
                "zoom": 1.0,
                "framing": "fit",
                "subtitles": True,
                "overlays": [],
            },
            "B": {
                "label": "dinamica",
                "start": 0.2,
                "end": duration,
                "zoom": 1.2,
                "framing": "crop-center",
                "subtitles": True,
                "overlays": [
                    {"start": 0.0, "end": 2.0, "text": "Hook real", "position": "top"}
                ],
            },
            "C": {
                "label": "experimental",
                "start": 0.0,
                "end": duration - 0.5,
                "zoom": 1.3,
                "framing": "fit",
                "subtitles": False,
                "freeze_end": 0.5,
                "overlays": [
                    {"start": 1.0, "end": 3.0, "text": "Remate", "position": "center"}
                ],
            },
        },
        "recommendation": "B",
        "hook": "Hook real",
        "caption": "Caption breve.",
        "privacy": ["revisar caras"],
        "publish": False,
    }


class VideoSocialTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.data_root = self.root / "jobs"
        self.source = self.root / "source.mp4"
        self.source.write_bytes(b"video-original")

    def tearDown(self):
        for path in self.root.rglob("original.*"):
            try:
                os.chmod(path, 0o600)
            except OSError:
                pass
        self.temporary.cleanup()

    def ingest(self, duration=12.0):
        with (
            mock.patch.object(MODULE.PREPARER, "probe_video", return_value=probe(duration=duration)),
            mock.patch.object(MODULE, "check_disk_space"),
        ):
            result = MODULE.ingest_video(self.source, self.data_root)
        return result, MODULE.job_path(self.data_root, result["job_id"])

    def analyze(self, job_dir):
        def fake_sheet(video, output, duration, mode):
            output.write_bytes(b"jpeg")

        with (
            mock.patch.object(MODULE, "create_contact_sheet", side_effect=fake_sheet),
            mock.patch.object(
                MODULE.PREPARER,
                "transcribe_video",
                return_value={
                    "language": "es",
                    "segments": [{"start": 0.0, "end": 2.0, "text": "Texto real"}],
                    "text": "Texto real",
                },
            ),
        ):
            return MODULE.analyze_job(job_dir, "base", False)

    def test_classifies_short_and_long_limits(self):
        self.assertEqual(MODULE.classify_video(60, MODULE.SHORT_MAX_BYTES), "short")
        self.assertEqual(MODULE.classify_video(61, MODULE.LONG_MAX_BYTES), "long")
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.classify_video(901, 1)
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.classify_video(30, MODULE.SHORT_MAX_BYTES + 1)

    def test_ingest_copies_original_and_preserves_source(self):
        source_checksum = MODULE.sha256_file(self.source)
        result, job_dir = self.ingest()
        state = MODULE.load_state(job_dir)
        copied = Path(state["source"]["original_path"])
        self.assertEqual(result["status"], "received")
        self.assertNotEqual(copied, self.source)
        self.assertEqual(MODULE.sha256_file(copied), source_checksum)
        self.assertEqual(MODULE.sha256_file(self.source), source_checksum)

    @unittest.skipIf(os.name == "nt", "Crear symlinks requiere privilegios adicionales en Windows.")
    def test_ingest_rejects_symlink(self):
        link = self.root / "link.mp4"
        link.symlink_to(self.source)
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_source_path(link)

    def test_rejects_sensitive_data_root_and_plan(self):
        sensitive = self.root / "secrets"
        sensitive.mkdir()
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_data_root(sensitive / "jobs")
        plan = sensitive / "plan.json"
        plan.write_text("{}", encoding="utf-8")
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_plan_file(plan)

    def test_analyze_generates_private_inputs_and_updates_state(self):
        _, job_dir = self.ingest()
        result = self.analyze(job_dir)
        analysis = MODULE.read_json(job_dir / "analysis" / "analysis.json")
        self.assertEqual(result["status"], "analyzed")
        self.assertEqual(result["transcript_segments"], 1)
        self.assertEqual(analysis["sharing_boundary"], "Solo transcripcion y hojas de fotogramas pueden enviarse al modelo configurado.")

    def test_plan_requires_narrative_reason_and_exact_variants(self):
        _, job_dir = self.ingest()
        state = MODULE.load_state(job_dir)
        cleaned = MODULE.validate_plan(valid_plan(), state)
        self.assertEqual(set(cleaned["variants"]), {"A", "B", "C"})
        missing = valid_plan()
        missing["selected_moment"]["reason"] = "corto"
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_plan(missing, state)

    def test_plan_rejects_zoom_overlays_duration_and_publication(self):
        _, job_dir = self.ingest()
        state = MODULE.load_state(job_dir)
        bad_zoom = valid_plan()
        bad_zoom["variants"]["B"]["zoom"] = 1.5
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_plan(bad_zoom, state)
        too_many = valid_plan()
        too_many["variants"]["A"]["overlays"] = [
            {"start": 0, "end": 1, "text": str(index), "position": "top"}
            for index in range(4)
        ]
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_plan(too_many, state)
        publishing = valid_plan()
        publishing["publish"] = True
        with self.assertRaises(MODULE.SocialVideoError):
            MODULE.validate_plan(publishing, state)

    def test_ffmpeg_command_is_argument_list_and_never_contains_overlay_text(self):
        variant = MODULE.validate_plan(
            valid_plan(),
            {
                "job_id": "video-20260824T000000Z-12345678",
                "metadata": {"duration_seconds": 12.0},
            },
        )["variants"]["B"]
        command = MODULE.build_ffmpeg_command(
            Path("/private/original.mp4"),
            Path("/private/B.mp4"),
            Path("/private/B.ass"),
            variant,
            {"width": 720, "height": 1280, "audio_present": True},
        )
        self.assertIsInstance(command, list)
        self.assertNotIn("Hook real", " ".join(command))
        self.assertEqual(command[0], "ffmpeg")
        self.assertNotIn("shell=True", " ".join(command))

    def test_render_versions_outputs_and_approve_preserves_checksum(self):
        source_checksum = MODULE.sha256_file(self.source)
        result, job_dir = self.ingest()
        self.analyze(job_dir)
        plan_file = self.root / "plan.json"
        plan_file.write_text(json.dumps(valid_plan()), encoding="utf-8")

        def fake_render(source, output, ass_file, variant, metadata):
            output.write_bytes(f"preview-{variant['label']}".encode())

        with (
            mock.patch.object(MODULE, "render_variant", side_effect=fake_render),
            mock.patch.object(
                MODULE,
                "verify_rendered_output",
                return_value={"duration_seconds": 5.3, "width": 720, "height": 1280},
            ),
        ):
            rendered = MODULE.render_job(job_dir, plan_file)
        self.assertEqual(rendered["status"], "rendered")
        self.assertEqual(set(rendered["outputs"]), {"A", "B", "C"})

        approved = MODULE.approve_job(job_dir, "b")
        self.assertEqual(approved["status"], "exported")
        self.assertEqual(approved["selected_variant"]["variant"], "B")
        self.assertEqual(
            MODULE.sha256_file(Path(approved["export"]["path"])),
            rendered["outputs"]["B"]["sha256"],
        )
        self.assertFalse(approved["published"])
        self.assertEqual(MODULE.sha256_file(self.source), source_checksum)

    def test_discard_marks_state_without_deleting_files(self):
        _, job_dir = self.ingest()
        original = Path(MODULE.load_state(job_dir)["source"]["original_path"])
        result = MODULE.discard_job(job_dir)
        self.assertEqual(result["status"], "discarded")
        self.assertTrue(original.exists())

    def test_status_uses_latest_active_job(self):
        first, first_dir = self.ingest()
        second, second_dir = self.ingest()
        first_state = MODULE.load_state(first_dir)
        first_state["updated_at"] = "2026-01-01T00:00:00+00:00"
        MODULE.write_private_json(MODULE.state_path(first_dir), first_state)
        second_state = MODULE.load_state(second_dir)
        second_state["updated_at"] = "2026-01-02T00:00:00+00:00"
        MODULE.write_private_json(MODULE.state_path(second_dir), second_state)
        result = MODULE.status_result(self.data_root, None)
        self.assertEqual(result["job_id"], second["job_id"])
        self.assertEqual(result["active_jobs"], 2)
        self.assertEqual(len(result["active_job_summaries"]), 2)
        self.assertEqual(result["active_job_summaries"][0]["job_id"], second["job_id"])
        self.assertEqual(result["active_job_summaries"][0]["original_name"], self.source.name)

    def test_retention_is_dry_run_and_does_not_delete(self):
        _, job_dir = self.ingest()
        state = MODULE.load_state(job_dir)
        state["status"] = "discarded"
        state["updated_at"] = "2026-01-01T00:00:00+00:00"
        MODULE.write_private_json(MODULE.state_path(job_dir), state)
        report = MODULE.retention_report(
            self.data_root,
            datetime(2026, 2, 1, tzinfo=timezone.utc),
        )
        self.assertEqual(report["candidate_count"], 1)
        self.assertFalse(report["changed"])
        self.assertTrue(job_dir.exists())


if __name__ == "__main__":
    unittest.main()
