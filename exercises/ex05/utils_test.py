"""Define unit tests for utils.py"""

__author__ = "730768692"

from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_1() -> None:
    """1: Use case for only_evens (tests what function should return)"""
    assert only_evens(a=[2, 3, 4]) == [2, 4]
    # The only even ints are 2 and 4 so we expect those values to be returned


def test_only_evens_2() -> None:
    """2: Use case for only_evens (tests how it should/should'nt mutate it's input)"""
    assert only_evens(a=[2, 2, 2]) == [2, 2, 2]
    # All ints are even, list a should NOT be modified, new list is returned


def test_only_evens_3() -> None:
    """3: Edge case for only_evens"""
    assert only_evens(a=[]) == []
    # Don't expect an empty list, no ints/no even ints so empty list is returned


def test_sub_1() -> None:
    """1: Use case for sub (tests what function should return)"""
    assert sub([3, 4, 5], 0, 2) == [3, 4]
    # 3 is at idx 0, 4 is at idx 1, the range is 0-1 so we expect those values returned


def test_sub_2() -> None:
    """2: Use case for sub (tests how it should/should'nt mutate it's input)"""
    assert sub([1, 2, 3, 4, 5], 0, 6) == [1, 2, 3, 4, 5]
    # All ints fit between idx range, list b should NOT be modified, new list returned


def test_sub_3() -> None:
    """3: Edge case for sub"""
    assert sub([6, 7, 8], -3, -1) == []
    # Don't expect idx range to be negative, no values fit between that range


def test_add_at_index_1() -> None:
    """1: Use case for add_at_index (tests what function should return)"""
    a: list[int] = [3, 4, 5, 7]
    # Reference
    # Need to create a varaible for the list because add_at_index returns None
    add_at_index(a, 6, 3)
    # Calling function with arguments
    assert a == [3, 4, 5, 6, 7]
    # Expecting a to change after being called
    # CANNOT DO: assert add_at_index([3, 4, 5, 7], 6, 3) == [3, 4, 5, 6, 7]
    # Won't work because add_at_index returns none and that's not equal to the list


def test_add_at_index_2() -> None:
    """2: Use case for add_at_index (tests how it should/should'nt mutate it's input)"""
    a: list[int] = [2, 3, 5]
    # Referance
    add_at_index(a, 4, 2)
    # Calling function with arguments
    assert a != [2, 3, 5]
    # List SHOULD be modified to [2, 3, 4, 5], should NOT stay the same


def test_add_at_index_3() -> None:
    """3: Edge case for add_at_index (tests that add_at_idex raises an IndexError)"""
    with pytest.raises(IndexError):
        a: list[int] = [1, 2, 4]
        add_at_index(a, 3, 5)
        # Asking the value 3 to be inserted at idx 5, when idx 5 does not exist
        # Expects an Index Error to be raised, if expection occurs as expected it passes
        # If exception is not raised, test will fail
