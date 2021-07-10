####################################################
# LeetCode Problem Number : 338
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/counting-bits/
####################################################
from typing import List


class CountBits:
    def calculate(self, n: int) -> List[int]:
        if n < 0:
            return []
        elif n == 0:
            return [0]
        elif n == 1:
            return [0, 1]

        ans = [0, 1]

        for i in range(2, n + 1):
            num_bits = 0
            """
            below loop will execute for the number of bits
            required to represent 'i'
            """
            while i:
                """
                check if LSB is set. if yes, then increment num_bits by 1
                """
                num_bits += i & 1
                """
                right shift by 1 bit to set the previous bit (bit to the left of LSB)
                as the new LSB
                """
                i >>= 1
            ans.append(num_bits)

        return ans

    def calculate_caching(self, n: int) -> List[int]:
        ans = [0]

        """
            in binary number system, multiplying a number by 2 is
            equivalent to adding a 0 to the end of its binary equivalent. That
            means :
                - number of 1's in 2N == number of 1's in N
                - number of 1's in (2N + 1) == number of 1's in N + 1

            this can also be expressed as :
                count_bit(N) [even number] = count_bit(N // 2) --> count_bit(N >> 1)
                count_bit(N) [odd number] = count_bit(N // 2) + 1 --> count_bit(N >> 1) + (N & 1)
        """
        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + (i & 1))

        return ans
