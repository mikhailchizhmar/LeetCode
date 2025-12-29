# https://leetcode.com/problems/rotate-array

# O(n), E(n)
def rotate1(nums: list[int], k: int) -> None:

    n = len(nums)
    k = k % n
    rotated = [0] * n

    for i in range(n):
        idx = (i + k) % n
        rotated[idx] = nums[i]

    for i in range(n):
        nums[i] = rotated[i]


# O(n), E(n)
def rotate2(nums: list[int], k: int) -> None:
    k %= len(nums)

    if k != 0:
        nums[:k], nums[k:] = nums[-k:], nums[:-k]


# O(n), E(1)
def rotate3(nums: list[int], k: int) -> None:
    k %= len(nums)

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)


# O(n^2), E(1)
def rotate_slow(nums: list[int], k: int) -> None:
    k = k % len(nums)
    while k > 0:
        prev = nums[-1]
        for i in range(len(nums)):
            curr = nums[i]
            nums[i] = prev
            prev = curr
        k -= 1


print(rotate3([1, 2, 3, 4, 5, 6, 7], 3))
