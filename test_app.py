import unittest
import app

class TestPythonApp(unittest.TestCase):
    
    def test_program_runs(self):
        # This executes the main function directly to verify it runs without crashing
        app.main()

if __name__ == "__main__":
    unittest.main()