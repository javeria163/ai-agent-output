# Solution

def reverse_string(s):
    return s[::-1]

# Tests

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("abcde") == "edcba"
    assert reverse_string("") == ""