import unittest
from unittest.mock import patch
from io import StringIO
import builtins
import importlib
import sys

class TestTallyCounter(unittest.TestCase):

    def run_main_with_inputs(self, inputs):
        # Patch input and stdout before importing main
        with patch.object(builtins, 'input', side_effect=inputs), \
             patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            if 'main' in sys.modules:
                importlib.reload(sys.modules['main'])
            else:
                import main
            return mock_stdout.getvalue()

    def test_run1_show_and_exit(self):
        output = self.run_main_with_inputs(['1', '0'])
        self.assertIn("Current count - 0", output)
        self.assertIn("Exiting program.", output)

    def test_run2_increase_and_show(self):
        output = self.run_main_with_inputs(['2', '1', '0'])
        self.assertIn("Count increased!", output)
        self.assertIn("Current count - 1", output)

    def test_run3_reset(self):
        output = self.run_main_with_inputs(['1', '2', '3', '1', '0'])
        self.assertIn("Cleared count!", output)
        self.assertIn("Current count - 0", output)

    def test_run4_unknown_option(self):
        output = self.run_main_with_inputs(['4', '0'])
        self.assertIn("Unknown option!", output)

    def test_run5_multiple_increases(self):
        output = self.run_main_with_inputs(['2', '2', '2', '1', '0'])
        self.assertIn("Current count - 3", output)

    def test_run6_invalid_inputs(self):
        output = self.run_main_with_inputs(['Show count', 'a', '1 - Show count', '1', '0'])
        self.assertEqual(output.count("Unknown option!"), 3)
        self.assertIn("Current count - 0", output)

if __name__ == '__main__':
    unittest.main()
