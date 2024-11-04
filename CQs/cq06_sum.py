"""Summing the elements if a list using different loops"""

__author__ = "730746935"


def w_sum(vals: list[float]) -> float:
    """Sum using while loop"""
    i: int = 0
    sum: float = 0.0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Sum using for in loop"""
    sum: float = 0.0
    for value in vals:
        sum += value
    return sum


def f_range_sum(vals: list[float]) -> float:
    sum: float = 0.0
    for value in range(0, len(vals)):
        sum += value
    return sum
