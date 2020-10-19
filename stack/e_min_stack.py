################################################
# LeetCode Problem Number : 155
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/min-stack/
################################################
class MinStack:
    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        """store every element as a tuple :
        (element, minimum stack element till that index position)
        """
        self.arr.append((x, min(self.getMin(), x)))

    def pop(self) -> None:
        if len(self.arr):
            self.arr.pop()

    def top(self) -> int:
        if len(self.arr):
            return self.arr[-1][0]

    def getMin(self) -> int:
        """ constant time operation """
        if len(self.arr):
            return self.arr[-1][1]
        else:
            return float("inf")
