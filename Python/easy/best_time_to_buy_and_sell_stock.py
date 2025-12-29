# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def max_profit(prices: list[int]) -> int:
    buy_price = float('inf')
    profit = 0

    for p in prices:
        if p <= buy_price:
            buy_price = p
        profit = max(profit, p - buy_price)

    return profit
