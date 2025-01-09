# https://leetcode.com/problems/max-consecutive-ones-ii

def main(nums: list[int]) -> int:
    max_len = 0
    l = r = 0
    d = {0: 0, 1: 0}
    while r < len(nums):
        d[nums[r]] += 1
        while l < r and d[0] > 1:
            d[nums[l]] -= 1
            l += 1
        if d[1] + d[0] > max_len:
            max_len = d[1] + d[0]
        r += 1

    return max_len


assert main([1, 1, 0, 1]) == 4
assert main([0, 1, 1, 1, 0, 1, 1, 0, 1]) == 6
assert main([1, 1, 1]) == 3
assert main([1, 1, 1, 0]) == 4
assert main([0, 0, 0, 0]) == 1
assert main([0, 0, 0, 1]) == 2
assert main([1, 1, 0, 0]) == 3
assert main([1 for _ in range(6404)]) == 6404
