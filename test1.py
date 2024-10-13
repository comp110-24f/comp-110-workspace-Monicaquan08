def extend(a: list[int], b: list[int]) -> None:
    """Append a list to the end of another list"""
    for item in b:
        a.append(item)
    print(a)


extend(a=[1, 3, 5], b=[2, 4, 6])
