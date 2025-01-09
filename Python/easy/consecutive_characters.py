# https://leetcode.com/problems/consecutive-characters

def maxPower(s: str) -> int:
    best_length = 1
    left = 0
    for right in range(len(s)):
        if s[left] != s[right]:
            left = right

        if right - left + 1 > best_length:
            best_length = right - left + 1

    return best_length
