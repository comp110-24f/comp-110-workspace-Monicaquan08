"""Summing the elements of a list using diffferent loops"""

__author__ = "730768692"


def w_sum(vals: list[float]) -> float:
    idx: int = 0
    sum: float = 0
    # Need to have another variable that keeps track of the sum that we can print
    while len(vals) > idx:
        sum += vals[idx]
        # Can use += to add values
        idx += 1
    return sum


def f_sum(vals: list[float]) -> float:
    # Don't need idx because for-in loop already iterates through every item
    sum: float = 0
    # Still need a variable to add values to
    for elem in vals:
        # Iterates through every item in the vals list
        sum += elem
        # Adding each item in the list to sum
    return sum


def f_range_sum(vals: list[float]) -> float:
    idx: int = 0
    # Need idx because for-in-range only works with the indices of the values
    sum: float = 0
    for idx in range(0, len(vals)):
        # Iterates through every idx in the range
        sum += vals[idx]
    return sum


print(f_range_sum([1.1, 0.9, 1.0]))
