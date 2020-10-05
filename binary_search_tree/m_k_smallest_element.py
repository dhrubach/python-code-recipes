####################################################################
# LeetCode Problem Number : 230
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/kth-smallest-element-in-a-bst/
####################################################################
from binary_search_tree.tree_node import TreeNode


class BinarySearchTree:
    # runtime -> 98.86%, memory -> 5.07%
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root:
            return 0

        res = 0
        pos = 0

        """ Inorder traversal of a binary search tree will
            return a sorted list of nodes

            Pick kth element from that list
        """

        def dfs(node: TreeNode):
            nonlocal res
            nonlocal pos

            if not node:
                return

            dfs(node.left)

            """ in each iteration, increase pos by 1. once it
                becomes equal to 'k', return corresponding node
            """
            pos = pos + 1
            if pos == k:
                res = node.val
                return

            dfs(node.right)

        dfs(root)
        return res
