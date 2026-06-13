# Solution

def add(a, b):
    return a + b

# Tests

def test_add():
    assert add(1, 2) == 3
    assert add(5, 7) == 12
    assert add(-3, 4) == 1
    assert add(0, 0) == 0
    assert add(-5, -8) == -13