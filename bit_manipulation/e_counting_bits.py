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
            while i:
                num_bits += i & 1
                i >>= 1
            ans.append(num_bits)

        return ans

    def calculate_caching(self, n: int) -> List[int]:
        ans = [0]

        for i in range(1, n + 1):
            ans.append(ans[i >> 1] + (i & 1))

        return ans
