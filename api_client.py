import requests
import json
from logger import Logger

class APIClient:
    """
    Client for interacting with the webhook API.
    """
    
    def __init__(self):
        """
        Initialize the API client with base URLs.
        """
        self.base_url = "https://bfhldevapigw.healthrx.co.in/hiring"
        self.logger = Logger()
        
    def generate_webhook(self, user_data):
        """
        Generate a webhook by sending a POST request.
        
        Args:
            user_data (dict): User information including name, regNo, and email.
            
        Returns:
            dict: Response data containing webhook URL and access token, or None if failed.
        """
        endpoint = f"{self.base_url}/generateWebhook/PYTHON"
        
        try:
            response = requests.post(
                endpoint,
                json=user_data,
                headers={"Content-Type": "application/json"}
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                self.logger.error(f"Failed to generate webhook. Status code: {response.status_code}")
                self.logger.error(f"Response: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            return None
            
    def submit_solution(self, webhook_url, access_token, sql_query):
        """
        Submit the SQL solution to the webhook.
        
        Args:
            webhook_url (str): URL to submit the solution to.
            access_token (str): Authentication token.
            sql_query (str): The SQL query solution.
            
        Returns:
            dict: Response data, or None if failed.
        """
        try:
            payload = {"finalQuery": sql_query}
            
            headers = {
                "Authorization": access_token,
                "Content-Type": "application/json"
            }
            
            response = requests.post(
                webhook_url,
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json()
            else:
                self.logger.error(f"Failed to submit solution. Status code: {response.status_code}")
                self.logger.error(f"Response: {response.text}")
                return None
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request failed: {str(e)}")
            return None
