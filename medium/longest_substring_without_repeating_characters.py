# https://leetcode.com/problems/longest-substring-without-repeating-characters

def length_of_longest_substring(s: str) -> int:
    if len(s) == 0:
        return 0

    window = {}
    max_len = 1
    l = 0
    for r in range(len(s)):
        window[s[r]] = window.get(s[r], 0) + 1
        while window[s[r]] > 1:
            window[s[l]] -= 1
            if window[s[l]] == 0:
                window.pop(s[l])
            l += 1
        if len(window) > max_len:
            max_len = len(window)
        # max_len = max(max_len, len(window))

    return max_len
