############################################################################
# LeetCode Problem Number : 581
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
############################################################################


class ShortestSubArray:
    # runtime - 76.59%, memory - 52.05%
    def findUnsortedSubarray(self, nums: [int]) -> (int, [int]):
        if not nums:
            return 0

        sarr = sorted(nums)
        start = end = -1
        index = -1

        """ iterate and compare between input and sorted array

            first index position which does not match -> start of sub-array
            last index position which does not match -> end of sub-array
        """
        for i, v in zip(nums, sarr):
            index += 1
            if i != v:
                """'start' is updated only once
                'end' follows the 'index' value
                """
                start = index if start == -1 else start
                end = index

        return (end - start + 1 if start != -1 else 0, sarr[end:start])

    def findUnsortedSubarray_concise(self, nums: [int]) -> int:
        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if not res else (res[-1] - res[0] + 1)

    def findUnsortedSubarray_no_sort(self, nums: [int]) -> int:
        start, end = 0, len(nums) - 1

        """ 'start' is the first index position where a number
            is out of increasing sort order
        """
        while start < len(nums) - 1 and nums[start] <= nums[start + 1]:
            start += 1

        """ check if input array is already sorted """
        if start == len(nums) - 1:
            return 0

        """ 'start' is the first index position where a number
            is out of increasing sort order calculated from the end
        """
        while end > 0 and nums[end] >= nums[end - 1]:
            end -= 1

        """ between start and end, get the least and maximum value
        """
        subMin, subMax = min(nums[start : end + 1]), max(nums[start : end + 1])

        """ check for values greater than minimum value to the left of 'start' index
            if present, include it in the sub-array
        """
        while start > 0 and nums[start - 1] > subMin:
            start -= 1

        """ check for values lesser than maximum value to the right of 'end' index
            if present, include it in the sub-array
        """
        while end < len(nums) - 1 and nums[end + 1] < subMax:
            end += 1

        return end - start + 1
