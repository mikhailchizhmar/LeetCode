# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii

def findMin(nums: list[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] < nums[r]:
            r = m
        else:
            r -= 1
    return nums[l]
