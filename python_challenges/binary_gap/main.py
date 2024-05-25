"""
Binary Gap Challenge
"""


def to_bin(n) -> str:
    """
    Method to get the binary representation from a positive number
    :param n: positive integer
    :return: binary representation of the number
    """
    return bin(n).replace("0b", "")


def solution(n) -> int:
    """
    Solution method for Binary Gap challenge
    :param n: positive integer
    :return: the length of its longest binary gap
    """
    n_bin = to_bin(n)
    if n_bin.count("1") == len(n_bin):
        return 0

    zero_max = 0
    count = 0
    for i in n_bin:
        if i == "1":
            zero_max = max(zero_max, count)
            count = 0
        else:
            count += 1

    return zero_max
