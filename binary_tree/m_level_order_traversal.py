########################################################################
# LeetCode Problem Number : 102
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/binary-tree-level-order-traversal/
########################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    """ level-order traversal

        visit all nodes at a particular level

            3
           / \
          9  20
            /  \
           15   7

        level - order -> [3, 9, 20, 15, 7]
    """

    # runtime -> 98.90%, memory -> 21.67%
    def levelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []

        res = []
        current_level = [root]

        while current_level:
            cval = []
            next_level = []

            for node in current_level:
                cval.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            res.append(cval)

            """ set next_level to the current_level for next iteration """
            next_level, current_level = current_level, next_level

        return res
