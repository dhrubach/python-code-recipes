#############################################################
# LeetCode Problem Number : 998
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/maximum-binary-tree-ii/
#############################################################
from binary_search_tree.tree_node import TreeNode


class MaxBinaryTree:
    def construct(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None

        if val > root.val:
            root = TreeNode(val, left=root)
        else:
            root.right = self.construct(root.right, val)

        return root
