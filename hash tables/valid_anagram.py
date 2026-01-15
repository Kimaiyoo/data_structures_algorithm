def is_anagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    return True


print(is_anagram('turn', 'entr'))
print(is_anagram('turn', 'untr'))


'''
Complexity:
Time Complexity:    O(N)
Space Complexity:   O(N)
'''