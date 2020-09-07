###############################################################
# LeetCode Problem Number : 938
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/range-sum-of-bst/
###############################################################

from binary_search_tree.tree_node import TreeNode


class RangeSumBST:
    def calculate(self, root: TreeNode, l: int, r: int):
        if not root:
            return 0

        return self.calculateRange(root, 0, l, r)

    def calculateRange(self, node: TreeNode, total: int, L: int, R: int) -> int:
        if not node:
            return total

        if node.val >= L and node.val <= R:
            """ if the current node value is in range, then add to the running total """
            total += node.val

        if node.val >= L:
            """ evaluate left sub-tree only if the current node value >= lower limit """
            total = self.calculateRange(node.left, total, L, R)

        if node.val <= R:
            """ evaluate right sub-tree only if the current node value <= upper limit """
            total = self.calculateRange(node.right, total, L, R)

        return total
