########################################################
# LeetCode Problem Number : 901
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/online-stock-span/
########################################################
class StockSpanner:
    def __init__(self):
        self.stack = []

    # runtime -> 91.50%, memory -> 6.73%
    def next(self, price: int) -> int:
        res = 1

        """ check if input price >= last recorded high price
            if yes, add span of that price to the current span
            remove previous price from stack

            with this, we don't store intermediate low stock prices
        """
        while self.stack and price >= self.stack[-1][0]:
            res += self.stack.pop()[1]

        """ store each price with its span """
        self.stack.append([price, res])

        """ return span for current input price """
        return res
