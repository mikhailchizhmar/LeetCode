# https://leetcode.com/problems/remove-element

def remove_element(nums: list[int], val: int) -> int:
    l = 0

    for r in range(len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1

    return l


assert remove_element([3, 2, 2, 3], 3) == 2
assert remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
assert remove_element([3, 3], 7) == 2
