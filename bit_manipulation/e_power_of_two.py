####################################################
# LeetCode Problem Number : 231
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/power-of-two/
###################################################
class PowerOfTwo:
    def calculate(self, n: int) -> bool:
        """
        An integer n is a power of two, if there exists an integer x such that n == pow(2, x)

        we also know the following about 'n':
            binary representation of 'n' will have only 1 bit set
            n & (n -1) returns n with the least set bit erased

        combining the two, it can be said that 'n' will be reduced to 0 after one
        such operation
        """
        return n > 0 and n & (n - 1) == 0
