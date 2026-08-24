import importlib.util
import os
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).parents[1] / "scripts" / "preparar-video-social.py"
SPEC = importlib.util.spec_from_file_location("preparar_video_social", SCRIPT_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class PrepareVideoSocialTests(unittest.TestCase):
    def test_parse_fraction(self):
        self.assertEqual(MODULE.parse_fraction("30/1"), 30.0)
        self.assertEqual(MODULE.parse_fraction("30000/1001"), 30000 / 1001)
        self.assertIsNone(MODULE.parse_fraction("0/0"))
        self.assertIsNone(MODULE.parse_fraction("invalid"))

    def test_summarize_probe(self):
        probe = {
            "format": {"duration": "12.5"},
            "streams": [
                {
                    "codec_type": "video",
                    "codec_name": "h264",
                    "width": 1080,
                    "height": 1920,
                    "avg_frame_rate": "30/1",
                },
                {"codec_type": "audio", "codec_name": "aac"},
            ],
        }
        result = MODULE.summarize_probe(probe, 1234)
        self.assertEqual(result["duration_seconds"], 12.5)
        self.assertEqual(result["width"], 1080)
        self.assertEqual(result["height"], 1920)
        self.assertTrue(result["audio_present"])

    def test_validate_video_accepts_small_supported_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "clip.mp4"
            path.write_bytes(b"video")
            self.assertEqual(MODULE.validate_video(path), path.resolve())

    def test_validate_video_rejects_unsupported_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "clip.txt"
            path.write_text("not a video", encoding="utf-8")
            with self.assertRaises(MODULE.VideoPreparationError):
                MODULE.validate_video(path)

    def test_validate_video_rejects_sensitive_path(self):
        with tempfile.TemporaryDirectory() as directory:
            sensitive = Path(directory) / "secrets"
            sensitive.mkdir()
            path = sensitive / "clip.mp4"
            path.write_bytes(b"video")
            with self.assertRaises(MODULE.VideoPreparationError):
                MODULE.validate_video(path)

    @unittest.skipIf(os.name == "nt", "Crear symlinks requiere privilegios adicionales en Windows.")
    def test_validate_video_rejects_symlink(self):
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "target.mp4"
            link = Path(directory) / "link.mp4"
            target.write_bytes(b"video")
            link.symlink_to(target)
            with self.assertRaises(MODULE.VideoPreparationError):
                MODULE.validate_video(link)


if __name__ == "__main__":
    unittest.main()
