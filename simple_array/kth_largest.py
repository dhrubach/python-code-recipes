######################################################################
# LeetCode Problem Number : 215
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/kth-largest-element-in-an-array/
######################################################################
from heapq import heapify, heappop


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

    def find_heap(self, nums: [int], k: int) -> int:
        """ using heap
            complexity : O(n + k log n)
                -> O(n) for creating the heap
                -> O(k logn) for popping 'k' elements
            space complecity : O(n)
        """
        if not nums:
            return None

        """ heapq.heapify, by default, will create a min-heap.

            Since we are looking for kth largest, multiply each
            element by -1 such that the original largest element
            becomes the root node. This will reduce the number of
            pop operations necessary to reach the kth largest element.
        """
        heap = [-num for num in nums]
        heapify(heap)

        """ pop `k-1` elements from the heap """
        for _ in range(k - 1):
            heappop(heap)

        """ root node is the answer. multiply by -1. """
        return -heappop(heap)
