###############################################################
# LeetCode Problem Number : 532
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/k-diff-pairs-in-an-array/
###############################################################
from collections import Counter


class KDiffPairs:
    # runtime -> 93.76%, memory -> 8.49%
    def findPairs(self, nums: [int], k: int) -> int:
        if k > 0:
            """create a list where each element is k-distance
            from corresponding element in the input list

            use set() to remove any duplicates

            input       -> 3 1 4 1 5
            kth array   -> 5 3 6 3 7
            """
            karr = set([i + k for i in nums])

            """ use set() intersection to find common elements between
                the 2 lists

                based on above example, c_elements -> {5, 3}

                hence only 2 unique pairs can be formed (1, 3) and (3, 5)
            """
            c_elements = set(nums) & set(karr)

            """ return length of the set """
            return len(c_elements)
        elif k == 0:
            """in case of zero distance, we only need to find
            out the number of distinct duplicate elements
            present in the list

            input -> 1 3 1 5 4 3
            distinct duplicates -> 1 and 3

            output of Counter(nums) -> [(1, 2), (3, 2), (5, 1), (4, 1)]
            answer -> number of unique elements which appear more than once in the list
            """
            return sum(i > 1 for i in Counter(nums).values())
        else:
            return 0
