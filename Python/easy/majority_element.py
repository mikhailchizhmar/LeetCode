# https://leetcode.com/problems/majority-element

def majority_element(nums: list[int]) -> int:
    d = {}
    for el in nums:
        d[el] = d.get(el, 0) + 1
        if d[el] > len(nums) / 2:
            return el


def majority_element2(nums: list[int]) -> int:
    res = majority = 0

    for n in nums:
        if majority == 0:
            res = n

        majority += 1 if n == res else -1

    return res
