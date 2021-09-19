import funcs


def test_add():
    assert funcs.add (4, 5) == 9


def test_mul():
    assert funcs.mul(10, 10) == 100


def test_dev():
    assert funcs.dev(10, 2) == 5
