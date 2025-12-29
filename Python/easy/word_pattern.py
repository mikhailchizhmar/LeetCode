# https://leetcode.com/problems/word-pattern

def word_pattern(pattern: str, s: str) -> bool:
    s_lst = s.split()
    if len(pattern) != len(s_lst):
        return False

    d = {}
    for p_c, s_c in zip(pattern, s_lst):
        if p_c not in d.keys():
            if s_c in d.values():
                return False
            d[p_c] = s_c
        elif d[p_c] != s_c:
            return False
    return True
