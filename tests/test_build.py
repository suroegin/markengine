import unittest
import build


class BuildTest(unittest.TestCase):
    def test_print_constant_variable(self):
        self.assertEqual((build.TEMPLATES_DIR / "base.html").name, "base.html")


if __name__ == "__main__":
    unittest.main()