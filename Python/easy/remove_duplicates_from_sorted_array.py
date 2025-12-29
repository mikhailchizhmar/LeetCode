# https://leetcode.com/problems/remove-duplicates-from-sorted-array

def remove_duplicates_improved(nums) -> int:
    i = 1

    for j in range(1, len(nums)):
        if nums[j] != nums[i - 1]:
            nums[i] = nums[j]
            i += 1

    return i


def remove_duplicates(nums) -> int:
    diff = 0
    i = 1
    while i < len(nums):
        while i < len(nums) and nums[i] == nums[i - 1]:
            diff += 1
            i += 1

        if i == len(nums):
            break
        nums[i - diff] = nums[i]
        i += 1
    return len(nums) - diff


assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert remove_duplicates([0, 0, 1, 1, 1]) == 2
