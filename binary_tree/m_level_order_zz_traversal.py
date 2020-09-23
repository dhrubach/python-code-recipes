###############################################################################
# LeetCode Problem Number : 103
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
###############################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    """ zigzag level-order traversal

        visit all nodes at a particular level

            3
           / \
          9  20
            /  \
           15   7

        level - order -> [3, 20, 9, 15, 7]
    """

    # runtime -> 97.96%, memory -> 57.66%
    def zigzagLevelOrder(self, root: TreeNode) -> [[int]]:
        if not root:
            return []

        res = []
        current_level = [root]
        ltor = True

        while current_level:
            cval = []
            next_level = []

            for node in current_level:
                cval.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            """ read all the nodes at a particular level from left to right

                reverse the level nodes every alternate level
            """
            res.append(cval if ltor else cval[::-1])
            ltor = False if ltor else True
            current_level = next_level

        return res
