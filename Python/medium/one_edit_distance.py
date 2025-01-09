# https://leetcode.com/problems/one-edit-distance

def is_one_edit_distance(s: str, t: str) -> bool:
    len_diff = abs(len(s) - len(t))
    if len_diff > 1:
        return False
    i = j = 0
    not_equal_once = False
    s_lt_t = len(s) < len(t)
    while i < len(s) and j < len(t):
        if s[i] != t[j]:
            if not_equal_once is False:
                not_equal_once = True
                if len_diff == 1:
                    if s_lt_t:
                        i -= 1
                    else:
                        j -= 1
            else:
                return False
        i += 1
        j += 1
    if len_diff == 0 and not_equal_once is False:
        return False
    return True


assert is_one_edit_distance("abc", "abec") is True
assert is_one_edit_distance("abc", "abedc") is False
assert is_one_edit_distance("", "a") is True
assert is_one_edit_distance("a", "") is True
assert is_one_edit_distance("aa", "") is False
assert is_one_edit_distance("aA", "ab") is True
assert is_one_edit_distance("adb", "aDb") is True
assert is_one_edit_distance("abc", "abC") is True
assert is_one_edit_distance("abcc", "abCC") is False
assert is_one_edit_distance("ab", "ab") is False
assert is_one_edit_distance("abcde", "bcde") is True
