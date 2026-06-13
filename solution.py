# Solution

def merge_sorted(l1, l2):
    result = []
    i = j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result += l1[i:]
    result += l2[j:]
    return result

# Tests

def test_merge_sorted():
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_sorted([1, 3, 5], []) == [1, 3, 5]
    assert merge_sorted([], [2, 4, 6]) == [2, 4, 6]
    assert merge_sorted([1, 3, 5], [1, 3, 5]) == [1, 1, 3, 3, 5, 5]