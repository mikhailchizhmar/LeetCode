# https://leetcode.com/problems/isomorphic-strings

def is_isomorphic(s: str, t: str) -> bool:
    d = {}
    for s_c, t_c in zip(s, t):
        if s_c not in d.keys():
            if t_c in d.values():
                return False
            d[s_c] = t_c
        elif d[s_c] != t_c:
            return False
    return True
