def add_at_index(c: list[int], element: int, idx: int) -> None:
    """Adds a specified element to a list at a specified index"""
    if idx < 0 or idx > len(c):
        # Tests if the idx is out of range
        raise IndexError("Index is out of bounds for the input list")
    c.insert(idx, element)
    # Inserts element into list BEFORE idx
    print(c)


add_at_index([1, 2, 4], 3, 2)
