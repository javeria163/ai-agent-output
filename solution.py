# Solution

def count_vowels(s):
    count = 0
    vowels = 'aeiou'
    for char in s:
        if char.lower() in vowels:
            count += 1
    return count

# Tests

def test_count_vowels():
    assert count_vowels('hello') == 2
    assert count_vowels('aeiou') == 5
    assert count_vowels('bcdfg') == 0
    assert count_vowels('AEIOU') == 5
    assert count_vowels('aEiOu') == 5