# https://leetcode.com/problems/subarray-sum-equals-k

def subarray_sum(nums: list[int], k: int) -> int:
    temp_sum = 0
    count = 0
    prefix_sums = {0: 1}
    for n in nums:
        temp_sum += n
        if temp_sum - k in prefix_sums:
            count += prefix_sums[temp_sum - k]

        prefix_sums[temp_sum] = prefix_sums.get(temp_sum, 0) + 1

    return count


assert subarray_sum([1, 1, 1], 2) == 2
assert subarray_sum([1, 2, 3], 3) == 2
assert subarray_sum([1, -1, 1], 1) == 3
assert subarray_sum([1], 1) == 1
assert subarray_sum([1], 125) == 0
assert subarray_sum([17, 7, 10, 7, 10], 17) == 4
assert subarray_sum([3, 3, 3, 3, 3], 3) == 5
assert subarray_sum([-3, -3, -3, -3, -3], -3) == 5
assert subarray_sum([-3, 3, -3, 3, 0], 0) == 7
assert subarray_sum([-1, 1, 0], 0) == 3
