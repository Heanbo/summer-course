def absolute_value(num: int) -> int:
    if num < 0:
        return -num
    return num


def test_absolute_value():
    assert absolute_value(5)
