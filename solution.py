# Solution

def longest_common_prefix(strs):
    if not strs:
        return ""
    shortest_str = min(strs, key=len)
    for i, char in enumerate(shortest_str):
        for string in strs:
            if string[i] != char:
                return shortest_str[:i]
    return shortest_str

# Tests

def test_longest_common_prefix():
    assert longest_common_prefix(["flower","flow","flight"]) == "fl"
    assert longest_common_prefix(["dog","racecar","car"]) == ""
    assert longest_common_prefix(["intership","interrupt","interior"]) == "inter"
    assert longest_common_prefix(["hello","hello","hello"]) == "hello"
    assert longest_common_prefix([]) == ""