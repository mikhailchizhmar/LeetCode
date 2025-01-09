# https://leetcode.com/problems/generate-parentheses

def generate_parentheses(n: int) -> list[str]:
    res = []

    def dfs(open_p, close_p, s):
        if open_p == close_p and open_p + close_p == n * 2:
            res.append(s)
            return

        if open_p < n:
            dfs(open_p + 1, close_p, s + "(")

        if close_p < open_p:
            dfs(open_p, close_p + 1, s + ")")

    dfs(0, 0, "")

    return res


assert generate_parentheses(2) == ['(())', '()()']
assert generate_parentheses(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']
