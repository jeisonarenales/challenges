"""
Unit tests for Binary Gap challenge
"""

import unittest
from binary_gap.main import to_bin, solution


class TestBinaryGap(unittest.TestCase):
    """
    Test class for Binary Gap challenge
    """

    def test_to_binary_method(self):
        """
        Tests binary method to return the correct binary representation of a number
        """
        self.assertEqual(to_bin(2), "10")
        self.assertEqual(to_bin(10), "1010")

    def test_solution(self):
        """
        Tests the solution of the challenge
        """
        self.assertEqual(solution(2), 0)  # 10
        self.assertEqual(solution(5), 1)  # 101
        self.assertEqual(solution(7), 0)  # 111
        self.assertEqual(solution(9), 2)  # 1001
        self.assertEqual(solution(15), 0)  # 1111
        self.assertEqual(solution(1041), 5)  # 10000010001
