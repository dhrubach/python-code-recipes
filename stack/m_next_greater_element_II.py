##############################################################
# LeetCode Problem Number : 503
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/next-greater-element-ii/
##############################################################
from typing import List


class NextGreaterElement:
    # runtime -> 69.04%, memory -> 57.32%
    def calculate(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res, monostack = [-1] * n, []

        """ since its a circular array, run the loop twice """
        for i in list(range(len(nums))) * 2:
            while monostack and nums[i] > nums[monostack[-1]]:
                x = monostack.pop()
                res[x] = nums[i]

            monostack.append(i)

        return res

    # runtime -> 98.56%, memory -> 57.32%
    def calculate_opm(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stack = nums[::-1]

        """ instead of running the loop twice as in the
            previous algorithm, start processing from the
            end of the input
        """
        for i in range(n - 1, -1, -1):
            """ since 'stack' is reverse of nums, it simulates
                a circular array
            """
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            if stack:
                ret[i] = stack[-1]
            """ store current element to the stack so that it
                can be used for future comparisons
            """
            stack.append(nums[i])

        return ret
