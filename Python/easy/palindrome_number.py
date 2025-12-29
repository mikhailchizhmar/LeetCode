# https://leetcode.com/problems/palindrome-number

def is_palindrome_improved(x: int) -> bool:
    if x < 0:
        return False

    reverse = 0
    x_copy = x

    while x > 0:
        reverse = (reverse * 10) + (x % 10)
        x //= 10

    return reverse == x_copy


def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    arr = []
    while x >= 0:
        arr.append(x % 10)
        x //= 10

    i = 0
    while i < len(arr) // 2 + 1:
        if arr[i] != arr[len(arr) - i - 1]:
            return False
        i += 1
    return True
