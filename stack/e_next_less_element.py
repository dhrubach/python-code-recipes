####################################################
# for each element in the list, return its distance
# from the 'next less element' (NLE). If an
# element does not have a NLE, return -1.
#
# uses a monotonous stack
###################################################
from typing import List


class NextLessElement:
    def calculate(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        right, monostack = [-1] * len(nums), []

        for i in range(len(nums)):
            """ check if the element pointed by the stack top
                is greater than the current element.

                if YES, then the current element is NLE of the
                element pointed by stack. Remove element from
                the stack and set its NLE

                how it differs from PLE?
                ------------------------
                PLE -> PLE of current element is set in the loop

                NLE -> NLE of element pointed by the stack is set in the loop
            """
            while monostack and nums[monostack[-1]] > nums[i]:
                x = monostack.pop()
                right[x] = i

            """ append current index to the stack """
            monostack.append(i)

        """ calculate the distance of each element from its NLE """
        for i in range(len(right)):
            right[i] = right[i] - i if right[i] != -1 else right[i]

        return right
