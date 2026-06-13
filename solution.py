# Solution

def power(base, exp):
    return base ** exp

# Tests

def test_power():
    assert power(2, 3) == 8
    assert power(2, 0) == 1
    assert power(2, -3) == 1/8
    assert power(0, 0) == 1
    assert power(10, 2) == 100