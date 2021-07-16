#############################################
# LeetCode Problem Number : 50
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/powx-n/
#############################################
class Powxn:
    def calculate(self, x: int, n: int) -> float:
        result, power = 1, n

        if power < 0:
            x, power = 1 / x, -n

        while power:
            if power & 1:
                result *= x
            x, power = x * x, power >> 1

        return result
