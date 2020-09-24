###############################################################
# LeetCode Problem Number : 139
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/sum-root-to-leaf-numbers/
###############################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value * 10 + node.right.val))
                if node.left:
                    stack.append((node.left, value * 10 + node.left.val))
        return res
