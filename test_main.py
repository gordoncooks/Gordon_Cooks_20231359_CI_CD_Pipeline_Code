# test_main.py

import unittest
from unittest.mock import patch  # Import patch to mock inputs and outputs
from io import StringIO          # Import StringIO to capture print output
import main                      # Import the main module to test

class TestGreetUser(unittest.TestCase):
    """
    This class contains unit tests for the greet_user function.
    It uses mocking to simulate user input and capture the printed output.
    """
    
    @patch('builtins.input', side_effect=['John', 'Doe'])  # Mock input to simulate user input
    @patch('sys.stdout', new_callable=StringIO)           # Mock stdout to capture print output
    def test_greet_user(self, mock_stdout, mock_input):
        """
        This test verifies that the greet_user function correctly greets
        the user by combining the first and last name.
        """
        main.greet_user()  # Call the function being tested
        self.assertEqual(mock_stdout.getvalue().strip(), "Hello, John Doe!")  
        # Assert that the printed output is as expected

if __name__ == '__main__':
    # This block ensures that the tests are run when this script is executed directly.
    unittest.main()
