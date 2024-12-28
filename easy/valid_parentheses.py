# https://leetcode.com/problems/valid-parentheses

def is_valid(s: str) -> bool:
    p = {")": "(", "}": "{", "]": "["}
    stack = []
    for c in s:
        if c in p.values():
            stack.append(c)
        else:
            if not stack or p[c] != stack.pop():
                return False

    return not stack


assert is_valid("((()))[]{}{[[[]]]}") is True
assert is_valid("((()))[]{}{[[[]]]") is False
assert is_valid("(]") is False
assert is_valid("]") is False
