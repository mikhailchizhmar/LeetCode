# https://leetcode.com/problems/ransom-note

def can_construct(ransom_note: str, magazine: str) -> bool:
    dict_m = {}
    dict_r = {}
    for c in magazine:
        dict_m[c] = dict_m.get(c, 0) + 1
    for c in ransom_note:
        dict_r[c] = dict_r.get(c, 0) + 1

    for letter, amount in dict_r.items():
        if letter not in dict_m.keys() or amount > dict_m[letter]:
            return False
    return True
