##########################################################
# LeetCode Problem Number : 654
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/maximum-binary-tree/
##########################################################
from binary_search_tree.tree_node import TreeNode


class MaxBinaryTree:
    """a maximum binary tree is one in which every node has a value
    which is greater than any value in its sub-tree
    """

    def construct(self, nums: [int]) -> TreeNode:
        if not nums or not len(nums):
            return None

        """ find maximum value and it's corresponding index
            present in input list. create a node which will
            represent root node of this sub-tree.

            example : input - [3,2,1,6,0,5]
                      mval - 6
                      idx - 3
        """
        mval = max(nums)
        idx = nums.index(mval)
        node = TreeNode(mval)

        """ check if a sub-array exists on the left of the
            max val. if yes, it will form LEFT sub-tree with
            its maximum value as the root node

            based on above example, left sub-array - [3,2,1],
            node - 3
        """
        if len(nums[:idx]):
            node.left = self.construct(nums[:idx])

        """ check if a sub-array exists on the right of the
            max val. if yes, it will form RIGHT sub-tree with
            its maximum value as the root node

            based on above example, left sub-array - [0,5],
            node - 5
        """
        if len(nums[idx + 1 :]):
            node.right = self.construct(nums[idx + 1 :])

        """ return root node """
        return node
