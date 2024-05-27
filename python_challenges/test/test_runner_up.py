"""
Unit tests for Runner-up
"""

import unittest
from runner_up.main import solution


class TestRunnerUp(unittest.TestCase):
    """
    Test class for Runner-up challenge
    """

    def test_solution(self):
        """
        Tests the solution of the challenge
        """
        self.assertEqual(solution(5, [2, 3, 6, 6, 5]), 5)
        self.assertEqual(solution(4, [57, 57, -57, 57]), -57)
