# https://leetcode.com/problems/merge-sorted-array

def merge(nums1, m, nums2, n):
    max_1 = m - 1
    max_2 = n - 1
    idx = m + n - 1

    while max_2 >= 0:
        if max_1 < 0 or nums2[max_2] >= nums1[max_1]:
            nums1[idx] = nums2[max_2]
            max_2 -= 1
        else:
            nums1[idx] = nums1[max_1]
            max_1 -= 1
        idx -= 1
    return nums1


assert merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
assert merge([1], 1, [], 0) == [1]
assert merge([0], 0, [1], 1) == [1]
assert merge([2, 0], 1, [1], 1) == [1, 2]



