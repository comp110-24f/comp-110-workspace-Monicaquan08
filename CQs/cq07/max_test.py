"""Practice writing unit tests"""

__author__ = "730768692"

from find_max import find_and_remove_max


def test_max() -> None:
    # Use case
    assert find_and_remove_max([1, 2, 3]) == 3
    # The expected return value is 3 because it is the largest int in the list


def test_mutates_max() -> None:
    # Use case
    b: list[int] = [4, 5, 6]
    # Must define a list to test
    find_and_remove_max(b)
    # Then call that list
    assert b == [4, 5]
    # Expect list b to be modified so the largest int is removed


def test_edge() -> None:
    # Edge case
    assert find_and_remove_max([]) == -1
    # Empty list is unconventional input but it's expected to return -1
