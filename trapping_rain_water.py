# https://leetcode.com/problems/trapping-rain-water

def trap(height: list[int]) -> int:
    max_pos = 0
    for i in range(len(height)):
        if height[i] > height[max_pos]:
            max_pos = i

    ans = 0
    curr_pos = 0
    for i in range(max_pos):
        if height[i] > curr_pos:
            curr_pos = height[i]
        ans += curr_pos - height[i]

    curr_pos = 0
    for i in range(len(height) - 1, max_pos, -1):
        if height[i] > curr_pos:
            curr_pos = height[i]
        ans += curr_pos - height[i]

    return ans


assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
