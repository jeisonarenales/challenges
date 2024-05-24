import unittest
from binary_gap.main import to_bin, solution
class TestBinaryGap(unittest.TestCase):
    def test_to_binary_method(self):
        self.assertEqual(to_bin(2), '10')
        self.assertEqual(to_bin(10), '1010')

    def test_solution(self):
        self.assertEqual(solution(2), 0) # 10
        self.assertEqual(solution(5), 1) # 101
        self.assertEqual(solution(7), 0) # 111
        self.assertEqual(solution(9), 2) # 1001
        self.assertEqual(solution(15), 0) # 1111
        self.assertEqual(solution(1041), 5) # 10000010001