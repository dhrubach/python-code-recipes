############################################################
# LeetCode Problem Number : 414
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/third-maximum-number/
############################################################
from typing import List


class ThirdLargestNumber:
    # runtime -> 97.90%, memory -> 83.47%
    # complexity -> time O(n), space O(1)
    def find(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        temp_list = [float("-inf"), float("-inf"), float("-inf")]

        for num in nums:
            if num not in temp_list:
                if num > temp_list[0]:
                    temp_list = [num, temp_list[0], temp_list[1]]
                elif num > temp_list[1]:
                    temp_list = [temp_list[0], num, temp_list[1]]
                elif num > temp_list[2]:
                    temp_list = [temp_list[0], temp_list[1], num]

        return max(temp_list) if float("-inf") in temp_list else temp_list[2]
