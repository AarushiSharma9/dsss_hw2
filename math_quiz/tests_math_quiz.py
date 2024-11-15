import unittest
from math_quiz import random_int, random_op, problem


class TestMathGame(unittest.TestCase):

    def test_random_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_op(self):
        # Test if the random operator generated is one of '+', '-', '*'
        operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random operators
            rand_op = random_op()
            self.assertIn(rand_op, operators)
        pass

    def test_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (8, 3, '-', '8 - 3', 5),
                (4, 6, '*', '4 * 6', 24)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem_str, answer = problem(num1, num2, operator)
                self.assertEqual(problem_str, expected_problem)
                self.assertEqual(answer, expected_answer)
                pass

if __name__ == "__main__":
    unittest.main()
