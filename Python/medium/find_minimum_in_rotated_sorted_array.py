# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

def findMin(nums: list[int]) -> int:
    if nums[0] <= nums[-1]:
        return nums[0]

    l = 0
    r = len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[0] <= nums[m]:
            l = m + 1
        else:
            r = m

    return nums[l]


# def main():
#     def can_place(cows, dist):
#         count = 1
#         last_pos = coords[0]
#
#         for i in range(1, len(coords)):
#             if coords[i] - last_pos >= dist:
#                 count += 1
#                 last_pos = coords[i]
#                 if count == cows:
#                     return True
#         return False
#
#     n, k = map(int, input().split())
#     coords = list(map(int, input().split()))
#     coords.sort()
#
#     left, right = 0, coords[-1] - coords[0]
#     answer = 0
#
#     while left <= right:
#         mid = (left + right) // 2
#         if can_place(k, mid):
#             answer = mid
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     print(answer)
#
#
# main()

def main():
    nums = list(map(int, input().split()))

    left, right = 1, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        count = sum(num <= mid for num in nums)

        if count > mid:
            right = mid
        else:
            left = mid + 1

    print(left)


main()