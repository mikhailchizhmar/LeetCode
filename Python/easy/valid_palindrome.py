# https://leetcode.com/problems/valid-palindrome

def is_palindrome2(s: str) -> bool:
    start = 0
    end = len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        elif s[start].lower() == s[end].lower():
            start += 1
            end -= 1
        else:
            return False

    return True


def is_palindrome(s: str) -> bool:
    new_s = ""
    for c in s.lower():
        if c.isalnum():
            new_s += c
    start = 0
    end = len(new_s) - 1
    while start <= (len(new_s) - 1) // 2:
        if new_s[start] != new_s[end]:
            return False
        start += 1
        end -= 1
    return True


assert is_palindrome("A man, a plan, a canal: Panama") is True
assert is_palindrome("race a car") is False
assert is_palindrome(" ") is True
