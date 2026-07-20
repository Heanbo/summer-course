from class_examples import add


def test_add():
    assert add(1, 2) == 3
    assert add(0, 5) == 5


def test_add_negative():
    assert add(-5, -7) == -12
    assert add(-5, 5) == 0
