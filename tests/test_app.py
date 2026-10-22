import io
import unittest
from contextlib import redirect_stdout

from app import main


class AppOutputTests(unittest.TestCase):
    def test_main_prints_build_confirmation(self):
        output = io.StringIO()
        with redirect_stdout(output):
            main()
        self.assertIn("Source code pulled successfully from GitHub!", output.getvalue())
        self.assertIn("Build execution complete.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
