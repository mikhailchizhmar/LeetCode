# https://leetcode.com/problems/merge-intervals

def merge(intervals: list[list[int]]) -> list[list[int]]:
    answer = []
    l = 0
    r = 1
    intervals.sort()
    while l < len(intervals):
        shift = 1
        answer.append(intervals[l])
        while r < len(intervals) and intervals[r][0] <= intervals[l][1]:
            answer[-1][1] = max(intervals[l][1], intervals[r][1])
            r += 1
            shift += 1
        r += 1
        l += shift

    return answer


assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
assert merge([[1, 3], [0, 5], [0, 4]]) == [[0, 5]]
assert merge([[1, 4], [0, 4]]) == [[0, 4]]
assert merge([[1, 4], [4, 5]]) == [[1, 5]]
assert merge([[1, 7]]) == [[1, 7]]
assert merge([[1, 4], [2, 3]]) == [[1, 4]]
