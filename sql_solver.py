class SQLSolver:
    """
    Solver for SQL problems based on the question number.
    """
    
    def solve_question(self, question_number):
        """
      
        
        Args:
            question_number (int): The question number (1 or 2).
            
        Returns:
            str: The SQL query solution, or None if an error occurs.
        """
        if question_number == 1:
            return self._solve_question_1()
        elif question_number == 2:
            return self._solve_question_2()
        else:
            return None
            
    def _solve_question_1(self):
        """
        Solution for Question 1 (odd registration numbers).
        
        Returns:
            str: The SQL query solution.
        """
        # The solution for Question 1
        # Question link: https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing
        
        # Sample SQL query - replace with actual solution
        sql_query = """
        SELECT 
            o.customer_id,
            c.name,
            COUNT(o.order_id) AS order_count,
            SUM(o.total_amount) AS total_amount_spent
        FROM orders o
        JOIN customers c ON o.customer_id = c.customer_id
        WHERE o.order_date BETWEEN '2023-01-01' AND '2023-12-31'
        GROUP BY o.customer_id, c.name
        HAVING COUNT(o.order_id) >= 3
        ORDER BY total_amount_spent DESC
        LIMIT 10;
        """
        
        # Real implementation would read the question and formulate the correct answer
        return sql_query.strip()
        
    def _solve_question_2(self):
        """
        Solution for Question 2 (even registration numbers).
        
        Returns:
            str: The SQL query solution.
        """
        # The solution for Question 2
        # Question link: https://drive.google.com/file/d/1P_O1ZvmDqAZJv77XRY_sV_ben11W_p2HV_b/view?usp=sharing
        
        # Sample SQL query - replace with actual solution
        sql_query = """
        SELECT 
            p.product_id,
            p.product_name,
            AVG(r.rating) AS average_rating,
            COUNT(r.review_id) AS review_count
        FROM products p
        LEFT JOIN reviews r ON p.product_id = r.product_id
        WHERE p.category = 'Electronics'
        GROUP BY p.product_id, p.product_name
        HAVING AVG(r.rating) > 4.0
        ORDER BY average_rating DESC, review_count DESC
        LIMIT 5;
        """
        
        # Real implementation would read the question and formulate the correct answer
        return sql_query.strip()
