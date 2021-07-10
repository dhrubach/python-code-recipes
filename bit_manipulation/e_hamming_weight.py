########################################################
# LeetCode Problem Number : 191
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/number-of-1-bits/
########################################################
class HammingWeight:
    def calculate(self, n: int) -> int:
        hweight = 0
        while n:
            """
            set the least set bit to 0 in each operation

            x & (x - 1) --> x with least set bit erased
            x & ~(x - 1) --> isolate least set bit in x i.e. set all other bits in x to '0'
            """
            n &= n - 1
            """
            increment count by 1
            """
            hweight += 1

        return hweight
