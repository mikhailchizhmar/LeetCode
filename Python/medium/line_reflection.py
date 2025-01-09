# https://leetcode.com/problems/line-reflection

def is_reflected_slow_incorrect(points: list[list[int]]) -> bool:
    def max_x(arr: list[list[int]]) -> list[int]:
        temp_max = arr[0]
        for x, y in arr:
            if x > temp_max[0]:
                temp_max = [x, y]
        return temp_max

    def min_x(arr: list[list[int]]) -> list[int]:
        temp_min = arr[0]
        for x, y in arr:
            if x < temp_min[0]:
                temp_min = [x, y]
        return temp_min

    if len(points) == 0:
        return True
    if len(points) == 1:
        return False
    mean = (max_x(points)[0] + min_x(points)[0]) / 2
    points_copy = points.copy()
    while len(points_copy) > 1:
        curr_max = max_x(points_copy)
        curr_min = min_x(points_copy)
        curr_mean = (curr_max[0] + curr_min[0]) / 2
        if curr_mean != mean:
            return False
        points_copy.remove(curr_max)
        points_copy.remove(curr_min)
    if len(points_copy) == 1 and points_copy[0][0] != mean:
        return False
    return True


def is_reflected(points: list[list[int]]) -> bool:
    if len(points) == 0:
        return True
    if len(points) == 1:
        return False

    mid = (len(points)) // 2
    first_half = sorted(points[:mid], key=lambda p: (p[0], -p[1]))
    second_half = sorted(points[mid:], key=lambda p: (p[0], p[1]))
    points_copy = first_half + second_half
    mean = (points_copy[0][0] + points_copy[-1][0]) / 2
    left = 0
    right = len(points_copy) - 1
    while left < right:
        curr_max = points_copy[right]
        curr_min = points_copy[left]
        curr_mean = (curr_min[0] + curr_max[0]) / 2
        if curr_mean != mean or curr_max[1] != curr_min[1]:
            return False
        left += 1
        right -= 1

    if left == right and points_copy[left][0] != mean:
        return False
    if len(points_copy) == 1 and points_copy[0][0] != mean:
        return False
    return True


# one more solution:
def is_reflected_stolen(points: list[list[int]]) -> bool:
    minX = float("inf")
    maxX = -float("inf")
    seen = set()

    for x, y in points:
        minX = min(minX, x)
        maxX = max(maxX, x)
        seen.add((x, y))

    summ = minX + maxX
    for x, y in points:
        if (summ - x, y) not in seen:
            return False
    return True


assert is_reflected([[1, 1], [-1, 1]]) is True
assert is_reflected([[1, 1]]) is False
assert is_reflected([]) is True
assert is_reflected([[0, 0], [1, 0], [3, 0]]) is False
assert is_reflected([[0,0],[1,1],[4,2],[9,3],[16,4],[25,5],[36,6],[49,7],
                     [64,8],[81,9],[0,0],[1,-1],[4,-2],[9,-3],[16,-4],
                     [25,-5],[36,-6],[49,-7],[64,-8],[81,-9]]) is False
