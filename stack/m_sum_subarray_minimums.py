###############################################################
# LeetCode Problem Number : 907
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/sum-of-subarray-minimums/
#
# Ref : https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
###############################################################
from typing import List
from stack.e_previous_less_element import PreviousLessElement
from stack.e_next_less_element import NextLessElement


class SubSubarrayMins:
    def calculate(self, A: List[int]) -> int:
        """ calculate PLE of each element in the input """
        ple = PreviousLessElement()
        left = ple.calculate(A)

        """ calculate NLE of each element in the input """
        nle = NextLessElement()
        right = nle.calculate(A)

        """ for an element whose either PLE or NLE does not exist,
            normalize it to :
                PLE -> index + 1
                NLE -> len(input) - index
        """
        for i in range(len(A)):
            left[i] = i + 1 if left[i] == -1 else left[i]
            right[i] = len(A) - i if right[i] == -1 else right[i]

        """ number of sub-arrays with A[i] as the minimum will be those which
                starts with any value between A[i] and PLE (since any value in between will be greater than A[i])
                number of such values = left[i]

                ends with any value between A[i] and NLE (since any value in between will be greater than A[i])
                number of such values = right[i]

            total number of sub-arrays = left[i] * right[i]

            since each of these sub-arrays will have A[i] as the minimum, its contribution to the overall sum
            will be A[i] * number of sub-arrays -> A[i] * (left[i] * right[i])
        """
        mod = (10 ** 9) + 7
        return sum(a * l * r for a, l, r in zip(A, left, right)) % mod
