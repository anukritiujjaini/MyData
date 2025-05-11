import unittest
import sys
import os

# Add the src directory to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sql_solver import SQLSolver

class TestSQLSolver(unittest.TestCase):
    """Test cases for the SQLSolver class."""
    
    def setUp(self):
        """Set up test environment."""
        self.sql_solver = SQLSolver()
        
    def test_solve_question_1(self):
        """Test solving question 1."""
        solution = self.sql_solver.solve_question(1)
        
        # Assertions
        self.assertIsNotNone(solution)
        self.assertIsInstance(solution, str)
        self.assertTrue(len(solution) > 0)
        
    def test_solve_question_2(self):
        """Test solving question 2."""
        solution = self.sql_solver.solve_question(2)
        
        # Assertions
        self.assertIsNotNone(solution)
        self.assertIsInstance(solution, str)
        self.assertTrue(len(solution) > 0)
        
    def test_invalid_question_number(self):
        """Test with an invalid question number."""
        solution = self.sql_solver.solve_question(3)
        
        # Assertions
        self.assertIsNone(solution)

if __name__ == '__main__':
    unittest.main()
