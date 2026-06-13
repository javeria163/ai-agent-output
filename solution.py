# Solution

def is_palindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

# Tests

def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Not a palindrome") == False
    assert is_palindrome("Was it a car or a cat I saw") == True
    assert is_palindrome("No 'x' in Nixon") == True