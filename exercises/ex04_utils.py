"""Practice using lists: comparing lists, finding max, comparing indexes, mutating"""

__author__ = "730768692"


def all(num_list: list[int], num: int) -> bool:
    """Checks if all the numbers in a list match a given num"""
    idx: int = 0
    count: int = 0
    while idx < len(num_list):
        # Allows us to loop through the num_list
        if num == num_list[idx]:
            count += 1
            # Keeps track of how many numbers match
        idx += 1
        # Need to check the other numbers in the list
    if len(num_list) == 0:
        return False
        # Returns False when the list is empty
    elif count == len(num_list):
        return True
        # Returns True when the instances of matching numbers match the len of the list
    else:
        return False
        # Returns False if the count does not match the len of list


def max(list: list[int]) -> int:
    """Finds the largest int in a list"""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    # If list is empty, max returns ValueError
    current_num: int = list[0]
    for item in list:
        # Iterates through every item in the list
        if item > current_num:
            current_num = item
        # Compares each number one by one to find the largest
    return current_num


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if every value at every index in equal in two lists"""
    if len(list_1) == len(list_2):
        # Condition to ensure lists are the same lenth
        idx: int = 0
        while idx < len(list_1):
            # Allows us to loop through lists
            if list_1[idx] == list_2[idx]:
                idx += 1
            else:
                return False
                # False if values are not equal at the same idx
        return True
    return False
    # False if the len of lists are not the same


def extend(a: list[int], b: list[int]) -> None:
    """Append a list to the end of another list"""
    for item in b:
        # Iterates through all items in list b
        a.append(item)
        # Appending every item in list b to the end of list a
    print(a)
    # Not returning anything, just printing list a
