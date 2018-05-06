import os
import unittest

class TextAnalysisTest(unittest.TestCase):
    """Tests for the ''analyze_test()'' function."""

    def setup(self):
        """Fixture that create a file for the text methods to use."""
        self.filename = 'text_analysis_test_file.txt'
        with open(self.filename, 'w') as f:
            f.write('Now we are engaged in a great civil war.\n'
                    "testing whether that nation,\n"
                    "or any nation so conceived and so dedicated,\n"
                    "can ling endure.")

    def tearDown(self):
        """Fixture that deletes the files used by the test methods."""
        try:
            os remove(self.filname)
        except:
            pass

    def test_function_runs(self):
        """Basic smoke test : does the function run."""
        analyze_text()

if __name__ == "__main__":
    unittest.main()
