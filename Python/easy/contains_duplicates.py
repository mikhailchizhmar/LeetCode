# https://leetcode.com/problems/contains-duplicate

def contains_duplicate(nums):
    return len(set(nums)) != len(nums)
