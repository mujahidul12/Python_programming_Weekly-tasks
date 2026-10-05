import unittest
import subprocess
import sys

class TestTemperatureConversionProgram(unittest.TestCase):

    def run_main(self, inputs):
        """Run main.py with simulated input and return output lines."""
        process = subprocess.Popen(
            [sys.executable, "main.py"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate("\n".join(inputs))
        return stdout.strip().splitlines()

    def test_celsius_to_fahrenheit(self):
        output = self.run_main(['1', '12.5'])
        found = any("12.5 °C equals to 54.5 °F" in line for line in output)
        self.assertTrue(found, f"Expected conversion line not found in output:\n{output}")

    def test_fahrenheit_to_celsius(self):
        output = self.run_main(['2', '77'])
        found = any("77.0 °F equals to 25.0 °C" in line for line in output)
        self.assertTrue(found, f"Expected conversion line not found in output:\n{output}")

    def test_exit_option(self):
        output = self.run_main(['0'])
        found = any("Exiting..." in line for line in output)
        self.assertTrue(found, f"'Exiting...' not found in output:\n{output}")

    def test_unknown_option(self):
        output = self.run_main(['9'])
        found = any("Unknown option." in line for line in output)
        self.assertTrue(found, f"'Unknown option.' not found in output:\n{output}")

if __name__ == '__main__':
    unittest.main()
