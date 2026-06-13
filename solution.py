# Solution

def is_anagram(s1, s2):
    return sorted(s1.replace(' ', '').lower()) == sorted(s2.replace(' ', '').lower())

# Tests

def test_is_anagram():
    assert is_anagram('Listen', 'Silent') == True
    assert is_anagram('Hello', 'World') == False
    assert is_anagram('Acts', 'CATS') == True
    assert is_anagram('Weird', 'Wired') == True
    assert is_anagram('Tom Marvolo Riddle', 'I am Lord Voldemort') == True