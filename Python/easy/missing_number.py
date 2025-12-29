# https://leetcode.com/problems/missing-number

def missing_number(nums: list[int]) -> int:
    n = len(nums)
    s = (0 + n) * (n + 1) // 2
    for el in nums:
        s -= el

    return s


def missing_number2(nums: list[int]) -> int:
    s = 0
    for i in range(len(nums)):
        s ^= nums[i]  # XOR
        s ^= i
    s ^= len(nums)
    return s
