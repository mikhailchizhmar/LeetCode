# https://leetcode.com/problems/largest-number
from functools import cmp_to_key


def largest_number(nums: list[int]) -> str:
    def compare(a, b):
        if a + b > b + a:
            return -1
        return 1
    nums = [str(num) for num in nums]
    nums.sort(key=cmp_to_key(compare))
    if nums[0] == '0':
        return '0'
    return ''.join(nums)
# [0, 0]


def largest_number2(nums: list[int]) -> str:
    for i in range(len(nums)):
        for j in range(len(nums) - i - 1):
            if str(nums[j]) + str(nums[j + 1]) > str(nums[j + 1]) + str(nums[j]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return ''.join([str(num) for num in nums])