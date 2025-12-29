
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

def remove_duplicates(nums: list[int]) -> int:
    curr_freq = 1
    l = 1
    r = 1
    while r < len(nums):
        if nums[r] != nums[r - 1]:
            curr_freq = 0

        curr_freq += 1
        if curr_freq <= 2:
            nums[l] = nums[r]
            l += 1
        r += 1

    return l


def remove_duplicates_easier(nums: list[int]) -> int:
    k = 2

    for i in range(2, len(nums)):
        if nums[i] != nums[k - 2]:
            nums[k] = nums[i]
            k += 1

    return k
