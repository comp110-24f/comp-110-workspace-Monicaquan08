"""Implement more list utility functions"""

__author__ = "730768692"


def only_evens(a: list[int]) -> list[int]:
    """Returns a list of even numbers in a list of ints"""
    even_list: list[int] = []
    # Empty list we can build on; add even ints to the list
    for elem in a:
        if elem % 2 == 0:
            even_list.append(elem)
            # Add to even_list
    return even_list


def sub(b: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Returns a list of ints between two indexs(excluding end index)"""
    sub_list: list[int] = []
    # Empty list we can build on; add ints at specified idx
    idx: int = 0

    while idx < len(b):
        if start_idx <= idx < end_idx:
            # Ensures we only see values between the start_idx and end_idx
            sub_list.append(b[idx])
            # Add to sub_list
        idx += 1
    return sub_list


def add_at_index(c: list[int], element: int, idx: int) -> None:
    """Adds a specified element to a list at a specified index"""
    if idx < 0 or idx > len(c):
        # Tests if the idx is out of range
        raise IndexError("Index is out of bounds for the input list")
    c.insert(idx, element)
    # Inserts element into list BEFORE idx
    print(c)
