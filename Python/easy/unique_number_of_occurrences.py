# https://leetcode.com/problems/unique-number-of-occurrences

def unique_occurrences(arr: list[int]) -> bool:
    d = {}
    for n in arr:
        d[n] = d.get(n, 0) + 1
    return len(set(d.values())) == len(d.values())
