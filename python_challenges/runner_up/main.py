"""
Runner-up Challenge
"""

from typing import List


def solution(n: int, score_list: List[int]) -> int:
    """
    Solution method for Runner-up challenge
    :param n: positive integer
    :param score_list: list with the scores
    :return: runner-up score
    """
    score_list = score_list[:n]

    return sorted(set(score_list))[-2]
