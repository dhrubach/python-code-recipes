######################################################################
# LeetCode Problem Number : 121
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
######################################################################
from typing import List


class BuySellStock:
    def calculate(self, prices: List[int]) -> int:
        max_profit, min_price_so_far = 0, prices[0]

        for i in range(1, len(prices)):
            max_profit_sell_today = prices[i] - min_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, prices[i])

        return max_profit
