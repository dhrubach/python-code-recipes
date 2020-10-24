####################################################
# for each element in the list, return its distance
# from the 'previous less element' (PLE). If an
# element does not have a PLE, return -1.
#
# uses a monotonous stack
###################################################
from typing import List


class PreviousLessElement:
    def calculate(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        left, monstack = [-1] * len(nums), []

        for i in range(len(nums)):
            """ if the element pointed by the stack top is
                greater than the current element, then pop
                the index from stack

                if the element pointed by the stack top is
                less than the current element, then it represents
                PLE of the current element
            """
            while monstack and nums[monstack[-1]] > nums[i]:
                monstack.pop()

            """ for a non-empty stack, stack top represents PLE """
            left[i] = -1 if not monstack else monstack[-1]

            """ append current index to the stack """
            monstack.append(i)

        """ calculate distance of each element from its PLE """
        for i in range(len(left)):
            left[i] = i - left[i] if left[i] != -1 else left[i]

        return left
