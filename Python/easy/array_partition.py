# https://leetcode.com/problems/array-partition

def array_pair_sum(nums: list[int]) -> int:
    nums = sorted(nums)
    return sum(nums[::2])
