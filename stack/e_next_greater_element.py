#############################################################
# LeetCode Problem Number : 496
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/next-greater-element-i/
#############################################################
from typing import List


class NextGreaterElement:
    # runtime -> 95.99%, memory -> 6.30%
    def calculate(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        right, monostack = {}, []

        for i in range(len(nums2)):
            while monostack and nums2[i] > nums2[monostack[-1]]:
                x = monostack.pop()
                right[nums2[x]] = nums2[i]

            monostack.append(i)

        for idx, x in enumerate(nums1):
            res[idx] = right.get(x, -1)

        return res
