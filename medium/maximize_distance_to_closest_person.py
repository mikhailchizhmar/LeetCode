# https://leetcode.com/problems/maximize-distance-to-closest-person

def max_dist_to_closest(seats: list[int]) -> int:
    res, prev = 0, -1
    for i, n in enumerate(seats):
        if n:
            dist = i if prev == -1 else (i - prev) // 2
            res = max(res, dist)
            prev = i

    if not seats[i]:  # check last seat edge-case
        res = max(res, i - prev)
    return res


print(max_dist_to_closest([1, 0, 0, 0, 1, 0, 1]))
print(max_dist_to_closest([1, 0, 0, 0]))
print(max_dist_to_closest([0, 1]))
