from funcs import get_first


def test_get_first() -> None:
    assert get_first([1, 2, 3]) == 1
