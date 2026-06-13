# Solution

def word_count(s):
    return len(s.split())

# Tests

def test_word_count():
    assert word_count("hello world") == 2
    assert word_count("this is a test") == 4
    assert word_count("") == 0
    assert word_count("single") == 1
    assert word_count("   space   ") == 1