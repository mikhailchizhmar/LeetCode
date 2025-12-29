# https://leetcode.com/problems/valid-anagram

# можно хранить один массив count_arr, для каждого char в s += 1,
# для каждого char в t -= 1. В конце return sum(count_arr) == 0
def is_anagram(s: str, t: str) -> bool:
    count_s = [0] * 26
    count_t = [0] * 26

    for char in s:
        count_s[ord(char) - ord('a')] += 1
    for char in t:
        count_t[ord(char) - ord('a')] += 1

    return count_s == count_t
