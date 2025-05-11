# Python Webhook Application

This application automates the process of generating a webhook, solving a SQL problem, and submitting the solution using the provided authentication token.

## Features

- Automatically generates a webhook on startup
- Determines which SQL problem to solve based on the registration number
- Solves the SQL problem and generates a query
- Submits the solution to the webhook URL using the authentication token
- Provides detailed logging throughout the process

## Setup

1. Make sure you have Python 3.6+ installed on your system

2. Install the required dependencies:
   ```
   pip install requests
   ```

3. Update the user configuration in `src/config.py` with your information:
   ```python
   USER_CONFIG = {
       "name": "Your Name",
       "regNo": "Your Registration Number",
       "email": "your.email@example.com"
   }
   ```

## Usage

Run the application using:

```
python src/main.py
```

Or use npm script:

```
npm start
```

## How It Works

1. On startup, the application sends a POST request to generate a webhook
2. Based on the response, it determines which SQL problem to solve (based on reg number)
3. It solves the SQL problem and generates a query
4. It submits the solution to the webhook URL using the authentication token

## Project Structure

- `src/main.py`: Entry point and orchestrator
- `src/api_client.py`: Handles API requests and responses
- `src/sql_solver.py`: Contains logic to solve SQL problems
- `src/config.py`: Stores configuration and user information
- `src/logger.py`: Provides logging functionality
