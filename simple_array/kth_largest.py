######################################################################
# LeetCode Problem Number : 215
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/kth-largest-element-in-an-array/
######################################################################
class KLargestElement:
    def find_bubble_sort(self, nums: [int], k: int) -> int:
        """ using bubble sort
            complexity : O(nk)
                -> outer loop `k` times, inner loop `n` times
        """
        if not nums:
            return None

        """ run outer loop `k` times, and not for `n` times
            since we only need to bubble kth largest element
            to its sorted place in the array
        """
        for i in range(k):
            """ for each iteration of outer loop, run inner
                loop one less than the number of elements in the array

                example : k = 2, len(nums) = 8
                          loop 1 : j -> range(7) [0 .. 6]
                          loop 2 : j -> range(6) [0 .. 5]
            """
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j + 1], nums[j] = nums[j], nums[j + 1]

        """ return kth largest element from the end """
        return nums[len(nums) - k]
