"""Practice writing a function that modifies a list"""

__author__ = "730768692"


def find_and_remove_max(a: list[int]) -> int:
    """Find the largest int in a list and remove it"""
    if len(a) > 0:
        max_num: int = a[0]
        for item in a:
            if item >= max_num:
                max_num = item
                # max_num must be written first to show that item becomes the new max

        idx: int = 0
        while idx < len(a):
            # Must have this condition to be able to loop
            if a[idx] == max_num:
                a.pop(idx)
                # Pop function uses a variable's index to remove
                # Every time an item is popped, the len(a) changes
                # When len(a) changes, the idx of each item changes too
                # So can't include idx+=1

            else:
                idx += 1
                # Only increases idx when len(a) stayes the same (nothing is popped)

        return max_num
    else:
        return -1
