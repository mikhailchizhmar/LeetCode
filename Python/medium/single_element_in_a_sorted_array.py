# https://leetcode.com/problems/single-element-in-a-sorted-array

def single_non_duplicate(nums: list[int]) -> int:
    n = len(nums)
    left = 0
    right = n - 1

    while left < right:
        mid = (left + right) // 2
        if mid % 2 != 0:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            left += 2
        else:
            right = mid

    return nums[left]


def func(nums):
    d = {}
    for el in nums:
        d[el] = d.get(el, 0) + 1

    for el, cnt in d.items():
        if cnt < 3:
            return el, cnt


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(*func(arr))


# main()

nums = list(map(int, input().split()))
n = len(nums) - 1

if n % 4 == 0:
    curr = n
elif n % 4 == 1:
    curr = 1
elif n % 4 == 2:
    curr = n + 1
else:
    curr = 0

for num in nums:
    curr ^= num

print(curr)
