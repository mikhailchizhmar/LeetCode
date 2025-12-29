# https://leetcode.com/problems/plus-one

def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += 1
        if digits[i] != 10:
            return digits
        digits[i] = 0

    return [1] + digits
