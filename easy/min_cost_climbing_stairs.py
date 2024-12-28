# https://leetcode.com/problems/min-cost-climbing-stairs

# Было на собеседовании
def min_cost_climbing_stairs(cost: list[int]) -> int:
    min_cost = [0] * (len(cost) + 1)
    for i in range(2, len(min_cost)):
        prev_1 = min_cost[i - 1] + cost[i - 1]
        prev_2 = min_cost[i - 2] + cost[i - 2]
        min_cost[i] = min(prev_1, prev_2)

    return min_cost[-1]
