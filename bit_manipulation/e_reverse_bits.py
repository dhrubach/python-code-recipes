###################################################
# LeetCode Problem Number : 190
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/reverse-bits/
###################################################
class ReverseBits:
    def alg_one(self, n: int) -> int:
        """
            - iterate through the bit string of the input integer, from right to left (i.e. n = n >> 1)
            - to retrieve the LSB of an integer, we apply the bit AND operation (n & 1)
            - for each bit, we reverse it to the correct position (i.e. (n & 1) << power)
            - accumulate this reversed bit to the final result
            - When there are no more 1's left (i.e. n == 0), we terminate the iteration
        """
        rev, pow = 0, 31
        while n:
            rev += (n & 1) << pow
            n = n >> 1
            pow -= 1

        return rev

    def alg_two(self, n: int) -> int:
        """
            motivation behind the below algorithm :

            for 8 bit binary number abcdefgh, the process is as follow:
            abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
        """
        n = (n >> 16) | (n << 16)
        n = ((n & 0xFF00FF00) >> 8) | ((n & 0x00FF00FF) << 8)
        n = ((n & 0xF0F0F0F0) >> 4) | ((n & 0x0F0F0F0F) << 4)
        n = ((n & 0xCCCCCCCC) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xAAAAAAAA) >> 1) | ((n & 0x55555555) << 1)

        return n
