from repo_template import MyClass


def test_sum():
    mc = MyClass(order=True)
    assert mc.sum(10, 34) == 44


def test_multiply():
    mc = MyClass(order=True)
    assert mc.multiply(10, 3) == 30
