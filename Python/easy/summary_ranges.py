# https://leetcode.com/problems/summary-ranges

def summary_ranges(nums):
    answer = []
    left = 0

    if len(nums) == 1:
        return [str(nums[0])]

    if len(nums) == 0:
        return nums

    numbers = nums.copy()

    # new number will not be included in the answer
    numbers.append(numbers[-1] + 100)

    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i - 1] != 1:
            if numbers[left] == numbers[i - 1]:
                answer.append(f"{numbers[left]}")
            else:
                answer.append(f"{numbers[left]}->{numbers[i - 1]}")
            left = i

    return answer


# more beautiful solution
def summary_ranges2(nums):
    ranges = []  # [start, end] or [x, y]
    for n in nums:
        if ranges and ranges[-1][1] == n - 1:
            ranges[-1][1] = n
        else:
            ranges.append([n, n])

    return [f'{x}->{y}' if x != y else f'{x}' for x, y in ranges]


assert summary_ranges2([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert summary_ranges2([0]) == ["0"]
assert summary_ranges2([]) == []
assert summary_ranges2([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
