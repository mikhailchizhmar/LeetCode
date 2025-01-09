# https://leetcode.com/problems/permutation-in-string

from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    window_size = len(s1)
    letters = Counter(s1)
    if len(s2) < len(s1):
        return False
    l = 0
    r = window_size - 1
    window = Counter(s2[l:r])
    while r < len(s2):
        window.update(s2[r])
        if window == letters:
            return True
        window.subtract(s2[l])
        l += 1
        r += 1

    return False


assert check_inclusion("ab", "eidbaooo") is True
assert check_inclusion("ab", "eidboaoo") is False
assert check_inclusion("a", "a") is True
assert check_inclusion("a", "") is False
assert check_inclusion("adc", "dcda") is True
