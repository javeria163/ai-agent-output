# Solution

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Tests

def test_flatten():
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]
    assert flatten([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert flatten([[1, [2, [3, [4, [5]]]]]]) == [1, 2, 3, 4, 5]
    assert flatten([]) == []