###########################################################################
# LeetCode Problem Number : 123
# Difficulty Level : Hard
# URL : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
##########################################################################
from typing import List


class BuySellStockTwice:
    def calculate(self, prices: List[int]) -> int:
        max_profit, min_price_so_far = 0, prices[0]
        first_buy_sell = [0] * len(prices)

        for i in range(1, len(prices)):
            max_profit_sell_today = prices[i] - min_price_so_far
            max_profit = max(max_profit, max_profit_sell_today)
            min_price_so_far = min(min_price_so_far, prices[i])
            first_buy_sell[i] = max_profit

        max_sell_so_far = float("-inf")
        for i, price in reversed(list(enumerate(prices[1:], 1))):
            max_sell_so_far = max(max_sell_so_far, price)
            max_profit = max(
                max_profit, max_sell_so_far - price + first_buy_sell[i - 1]
            )

        return max_profit
