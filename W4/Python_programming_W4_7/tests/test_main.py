import unittest
import subprocess

class TestMultiplicativePersistence(unittest.TestCase):
    def run_script_with_input(self, user_input):
        result = subprocess.run(
            ['python3', 'main.py'],
            input=user_input,
            text=True,
            capture_output=True
        )
        return result.stdout

    def test_input_679(self):
        expected = (
            "Program starting.\n\n"
            "Check multiplicative persistence.\n"
            "Insert an integer: 6 * 7 * 9 = 378\n"
            "3 * 7 * 8 = 168\n"
            "1 * 6 * 8 = 48\n"
            "4 * 8 = 32\n"
            "3 * 2 = 6\n"
            "No more steps.\n\n"
            "This program took 5 step(s)\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("679\n")
        self.assertEqual(output, expected)

    def test_input_123456789(self):
        expected = (
            "Program starting.\n\n"
            "Check multiplicative persistence.\n"
            "Insert an integer: 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 = 362880\n"
            "3 * 6 * 2 * 8 * 8 * 0 = 0\n"
            "No more steps.\n\n"
            "This program took 2 step(s)\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("123456789\n")
        self.assertEqual(output, expected)

    def test_input_999(self):
        expected = (
            "Program starting.\n\n"
            "Check multiplicative persistence.\n"
            "Insert an integer: 9 * 9 * 9 = 729\n"
            "7 * 2 * 9 = 126\n"
            "1 * 2 * 6 = 12\n"
            "1 * 2 = 2\n"
            "No more steps.\n\n"
            "This program took 4 step(s)\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("999\n")
        self.assertEqual(output, expected)

    def test_input_101(self):
        expected = (
            "Program starting.\n\n"
            "Check multiplicative persistence.\n"
            "Insert an integer: 1 * 0 * 1 = 0\n"
            "No more steps.\n\n"
            "This program took 1 step(s)\n\n"
            "Program ending.\n"
        )
        output = self.run_script_with_input("101\n")
        self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
