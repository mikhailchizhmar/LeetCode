# https://leetcode.com/problems/find-all-anagrams-in-a-string

def find_anagrams(s, p):
    if len(s) < len(p):
        return []

    origin = {}
    for c in p:
        origin[c] = origin.get(c, 0) + 1

    w_size = len(p)
    window = {}
    for i in range(w_size):
        window[s[i]] = window.get(s[i], 0) + 1

    answer = []
    for i in range(len(s) - w_size + 1):
        if window == origin:
            answer.append(i)

        if i + w_size < len(s):
            window[s[i]] -= 1
            if window[s[i]] == 0:
                window.pop(s[i])
            window[s[i + w_size]] = window.get(s[i + w_size], 0) + 1

    return answer


def find_anagrams2(s, p):
    if len(s) < len(p):
        return []

    origin = {}
    for c in p:
        origin[c] = origin.get(c, 0) + 1

    w_size = len(p)
    window = {}
    for i in range(w_size):
        window[s[i]] = window.get(s[i], 0) + 1

    answer = [0] if window == origin else []
    for i in range(w_size, len(s)):
        old_char = s[i - w_size]
        window[old_char] -= 1
        if window[old_char] == 0:
            window.pop(old_char)

        new_char = s[i]
        window[new_char] = window.get(new_char, 0) + 1

        if window == origin:
            answer.append(i - w_size + 1)

    return answer


assert find_anagrams2("cbaebabacd", "abc") == [0, 6]
assert find_anagrams2("abab", "ab") == [0, 1, 2]
assert find_anagrams2("a", "abcd") == []
assert find_anagrams2("g", "g") == [0]
assert find_anagrams2("g", "f") == []
