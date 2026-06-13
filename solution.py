# Solution

def find_max(lst):
    if len(lst) == 0:
        return None
    return max(lst)

# Tests

def test_find_max():
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3, -4, -5]) == -1
    assert find_max([]) == None
    assert find_max([5]) == 5
    assert find_max([5, 5, 5, 5]) == 5