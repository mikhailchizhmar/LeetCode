# https://leetcode.com/problems/two-sum

def two_sum(nums: list[int], target: int) -> list[int]:
    map = {}
    for i in range(len(nums)):
        n = target - nums[i]
        if n not in map.keys():
            map[nums[i]] = i
        else:
            return [map[n], i]
    return []


assert two_sum([2,7,11,15], 9) == [0, 1]
assert two_sum([3,2,4], 6) == [1, 2]
assert two_sum([3,3], 6) == [0, 1]
