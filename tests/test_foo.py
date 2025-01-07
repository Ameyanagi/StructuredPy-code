from structuredpy_code.foo import add, foo


def test_foo():
    assert foo("foo") == "foo"


def test_add():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, -2) == -3


def test_add_zero():
    assert add(0, 0) == 0


def test_add_float():
    assert add(1.5, 2.5) == 4.0
