#################################################
# LeetCode Problem Number : 494
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/target-sum/
#################################################
from typing import List
from collections import defaultdict


class TargetSum:
    def calculate_hashmap(self, nums: List[int], S: int) -> int:
        """initialize a hashmap to capture the count of
        all possible sum

        key --> represents the cumulative sum
        value --> count

        example :
            count = { 0: 3, -1: 2 }
            interpretation: 3 ways to arrive at sum 0
                            2 ways to arrive at sum -1
        """
        count = defaultdict(int)

        count[0] = 1

        """ iterate over input numbers list"""
        for x in nums:
            """initialize temp hashmap to capture counts
            as each item from input list is processed

            example :

            input = [1, 1, 1, 1, 1]
            S = 3

            after procesing first 2 items i.e. [1, 1],
            count = {2: 1, 0: 2, -2: 1}
            breakup : sum(2) -> +1+1
                      sum(0) -> +1-1, -1+1
                      sum(-2) -> -1-1
            """
            step = defaultdict(int)

            for y in count:
                """step 1 : (y +- x) add current item to the running sum
                step 2 : check if computed sum is already present in hashmap
                step 3 : add the counts for that sum

                example :
                x -> 1, y -> 0
                step[y + x] -> step[0 + 1] -> step [1] = 1 (computed earlier)
                count[y] -> count[0] = 2 (computed earlier)
                step[1] = step[1] + count[0] = 1 + 2 = 3

                i.e there are 3 ways to arrive at a sum of 1 using [1, 1, 1]
                sum(1) -> +1-1+1, -1+1+1, +1+1-1
                """
                step[y + x] += count[y]
                step[y - x] += count[y]

            count = step

        """ return count of input sum """
        return count[S]
