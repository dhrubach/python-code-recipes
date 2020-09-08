######################################################################
# LeetCode Problem Number : 700
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/search-in-a-binary-search-tree/
#####################################################################
from binary_search_tree.tree_node import TreeNode


class BinarySearchTree:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if root.val == val:
            return root

        if val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

