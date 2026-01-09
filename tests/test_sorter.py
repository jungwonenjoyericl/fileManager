# src/test_sorter.py

import tempfile
import unittest
from pathlib import Path

from src.config import CATEGORY_MAP, UNKNOWN_FOLDER
from src.sorter import create_folders, categorize_files_by_type


class TestSorter(unittest.TestCase):
    def test_categorize_copies_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "input"
            output_dir = Path(tmpdir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            (input_dir / "photo.jpg").write_text("img")
            (input_dir / "movie.mp4").write_text("vid")
            (input_dir / "notes.txt").write_text("doc")
            (input_dir / "mystery.bla").write_text("unknown")

            create_folders(str(input_dir), str(output_dir), CATEGORY_MAP, False)
            categorize_files_by_type(str(input_dir), str(output_dir), CATEGORY_MAP)

            self.assertTrue((output_dir / "Images" / "photo.jpg").is_file())
            self.assertTrue((output_dir / "Videos" / "movie.mp4").is_file())
            self.assertTrue((output_dir / "Documents" / "notes.txt").is_file())
            self.assertTrue((output_dir / UNKNOWN_FOLDER / "mystery.bla").is_file())

    def test_create_folders_all(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            input_dir = Path(tmpdir) / "input"
            output_dir = Path(tmpdir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()

            create_folders(str(input_dir), str(output_dir), CATEGORY_MAP, True)

            for name in CATEGORY_MAP.keys():
                self.assertTrue((output_dir / name).is_dir())
            self.assertTrue((output_dir / UNKNOWN_FOLDER).is_dir())


if __name__ == "__main__":
    unittest.main()