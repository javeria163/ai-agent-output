# Solution

def sum_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

# Tests

def test_sum_digits():
    assert sum_digits(123) == 6
    assert sum_digits(-123) == 6
    assert sum_digits(0) == 0
    assert sum_digits(100) == 1
    assert sum_digits(-100) == 1