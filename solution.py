# Solution

def remove_duplicates(lst):
    return sorted(set(lst))

# Tests

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5, 6, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert remove_duplicates(['a', 'b', 'b', 'c', 'c', 'd']) == ['a', 'b', 'c', 'd']
    assert remove_duplicates([]) == []