import unittest
from unittest.mock import patch
from io import StringIO
import subprocess
import sys

class TestMainScript(unittest.TestCase):

    def run_script_with_input(self, inputs):
        """Run main.py as a subprocess with simulated input and capture output."""
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input="\n".join(inputs))
        return stdout, stderr

    def test_exit_main_menu(self):
        stdout, _ = self.run_script_with_input(['0'])
        self.assertIn("Exiting...", stdout)
        self.assertIn("Program ending.", stdout)

    def test_meters_to_kilometers(self):
        stdout, _ = self.run_script_with_input(['1', '1', '1000'])
        self.assertIn("1000.0 m is 1.0 km", stdout)

    def test_kilometers_to_meters(self):
        stdout, _ = self.run_script_with_input(['1', '2', '20'])
        self.assertIn("20.0 km is 20000.0 m", stdout)

    def test_length_unknown_option(self):
        stdout, _ = self.run_script_with_input(['1', '3'])
        self.assertIn("Unknown option.", stdout)

    def test_length_exit(self):
        stdout, _ = self.run_script_with_input(['1', '0'])
        self.assertIn("Exiting...", stdout)

    def test_grams_to_pounds(self):
        stdout, _ = self.run_script_with_input(['2', '1', '100'])
        self.assertIn("100.0 g is 0.2 lb", stdout)

    def test_pounds_to_grams(self):
        stdout, _ = self.run_script_with_input(['2', '2', '1'])
        self.assertIn("1.0 lb is 453.6 g", stdout)

    def test_weight_unknown_option(self):
        stdout, _ = self.run_script_with_input(['2', '3'])
        self.assertIn("Unknown option.", stdout)

    def test_weight_exit(self):
        stdout, _ = self.run_script_with_input(['2', '0'])
        self.assertIn("Exiting...", stdout)

    def test_main_unknown_option(self):
        stdout, _ = self.run_script_with_input(['9'])
        self.assertIn("Unknown option.", stdout)

if __name__ == '__main__':
    unittest.main()
