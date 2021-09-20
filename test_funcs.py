import funcs


def test_add():
    assert funcs.add(4, 5) == 9


def test_mul():
    assert funcs.mul(3, 'Hello ') == 'Hello Hello Hello '
    print(funcs.mul(3, 'Hello'), "PASSED")


def test_dev():
    assert funcs.dev(10, 2) == 5


def test_sub():
    assert funcs.sub(10, 10) == 0


def test_str():
    string = funcs.str('he')
    assert type(string) is str
