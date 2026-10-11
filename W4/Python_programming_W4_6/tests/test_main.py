import unittest
from unittest.mock import patch
from io import StringIO
import subprocess
import os

class TestCollatzConjecture(unittest.TestCase):
    def run_script_with_input(self, user_input):
        result = subprocess.run(
            ['python3', 'main.py'],
            input=user_input,
            text=True,
            capture_output=True
        )
        return result.stdout

    def test_input_10(self):
        expected = (
            "Program starting.\n"
            "Insert a positive integer: 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n"
            "Sequence had 6 total steps.\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("10\n")
        self.assertEqual(output, expected)

    def test_input_6(self):
        expected = (
            "Program starting.\n"
            "Insert a positive integer: 6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n"
            "Sequence had 8 total steps.\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("6\n")
        self.assertEqual(output, expected)

    def test_input_7(self):
        expected = (
            "Program starting.\n"
            "Insert a positive integer: 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1\n"
            "Sequence had 16 total steps.\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("7\n")
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
