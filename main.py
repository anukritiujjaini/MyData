import sys
from api_client import APIClient
from config import USER_CONFIG
from sql_solver import SQLSolver
from logger import Logger

def main():
    """
    Main function that orchestrates the webhook flow.
    """
    logger = Logger()
    logger.info("Starting webhook application...")
    
    try:
        # Initialize API client
        api_client = APIClient()
        
        # Step 1: Generate webhook
        logger.info("Generating webhook...")
        webhook_data = api_client.generate_webhook(USER_CONFIG)
        
        if not webhook_data:
            logger.error("Failed to generate webhook. Exiting.")
            return 1
            
        logger.success(f"Webhook generated successfully!")
        logger.info(f"Webhook URL: {webhook_data['webhook']}")
        
        # Step 2: Determine which question to solve based on regNo
        reg_no = USER_CONFIG["regNo"]
        last_digit = int(reg_no[-1])
        question_number = 1 if last_digit % 2 != 0 else 2
        
        logger.info(f"Based on registration number {reg_no}, solving Question {question_number}")
        
        # Step 3: Solve the SQL problem
        sql_solver = SQLSolver()
        solution = sql_solver.solve_question(question_number)
        
        if not solution:
            logger.error("Failed to solve the SQL problem. Exiting.")
            return 1
            
        logger.success("SQL solution generated!")
        logger.info(f"Solution query: {solution}")
        
        # Step 4: Submit the solution
        logger.info("Submitting solution to webhook...")
        submission_result = api_client.submit_solution(
            webhook_data["webhook"],
            webhook_data["accessToken"],
            solution
        )
        
        if submission_result:
            logger.success("Solution submitted successfully!")
            logger.info(f"Response: {submission_result}")
            return 0
        else:
            logger.error("Failed to submit solution.")
            return 1
            
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
