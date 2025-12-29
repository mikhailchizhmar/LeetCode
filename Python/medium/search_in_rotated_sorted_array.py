# https://leetcode.com/problems/search-in-rotated-sorted-array

def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[left] <= nums[mid]:  # 0..m - рост, m..n - минимум
            if nums[left] <= target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid
            else:
                right = mid - 1

    return left if nums[left] == target else -1


assert search([5, 1, 3], 1) == 1
