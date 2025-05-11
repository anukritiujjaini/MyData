import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from api_client import APIClient

class TestAPIClient(unittest.TestCase):
    """Test cases for the APIClient class."""
    
    def setUp(self):
        """Set up test environment."""
        self.api_client = APIClient()
        self.user_data = {
            "name": "Anukriti Ujjainiya",
            "regNo": "0827AL221029",
            "email": "anukritiujjainiya@acropolis.in"
        }
        
    @patch('requests.post')
    def test_generate_webhook_success(self, mock_post):
        """Test successful webhook generation."""
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "webhook": "https://webhook.site/5adf9848-b71c-4f50-98b4-c84f9cef6a65",
            "accessToken": "token123"
        }
        mock_post.return_value = mock_response
        
        # Call the method
        result = self.api_client.generate_webhook(self.user_data)
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result["webhook"], "https://webhook.site/5adf9848-b71c-4f50-98b4-c84f9cef6a65")
        self.assertEqual(result["accessToken"], "token123")
        
    @patch('requests.post')
    def test_generate_webhook_failure(self, mock_post):
        """Test webhook generation failure."""
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.text = "Bad Request"
        mock_post.return_value = mock_response
        
        # Call the method
        result = self.api_client.generate_webhook(self.user_data)
        
        # Assertions
        self.assertIsNone(result)
        
    @patch('requests.post')
    def test_submit_solution_success(self, mock_post):
        """Test successful solution submission."""
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success"}
        mock_post.return_value = mock_response
        
        # Call the method
        result = self.api_client.submit_solution(
            "https://webhook.site/5adf9848-b71c-4f50-98b4-c84f9cef6a65",
            "token123",
            "SELECT * FROM users"
        )
        
        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result["status"], "success")
        
    @patch('requests.post')
    def test_submit_solution_failure(self, mock_post):
        """Test solution submission failure."""
        # Mock response
        mock_response = MagicMock()
        mock_response.status_code = 401
        mock_response.text = "Unauthorized"
        mock_post.return_value = mock_response
        
        # Call the method
        result = self.api_client.submit_solution(
            "https://webhook.site/5adf9848-b71c-4f50-98b4-c84f9cef6a65k",
            "invalid_token",
            "SELECT * FROM users"
        )
        
        # Assertions
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
