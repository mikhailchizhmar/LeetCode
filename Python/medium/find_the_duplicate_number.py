# https://leetcode.com/problems/find-the-duplicate-number

def find_duplicate(nums: list[int]) -> int:
    left, right = 1, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        count = sum(num <= mid for num in nums)

        if count > mid:
            right = mid
        else:
            left = mid + 1

    return left
