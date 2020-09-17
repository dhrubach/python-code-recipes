####################################################################
# LeetCode Problem Number : 589
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/n-ary-tree-preorder-traversal/
####################################################################

from binary_tree.node import Node


class PreorderTreeTraversal:
    def traverse(self, root: Node) -> [int]:
        if not root:
            return []

        """ create an empty list to record elements under a sub-tree """
        res = []

        """ insert root node of current sub-tree """
        res.append(root.val)

        """ check for leaf node """
        if root.children:
            for ch in root.children:
                """ for each child node, traverse its sub-tree """
                res += self.traverse(ch)

        """ return traversed nodes of a sub-tree """
        return res

    def traverse_iterative(self, root: Node) -> [int]:
        if not root:
            return []

        res = []
        """ start iteration by inserting root node into the stack """
        stack = [root]

        while stack:
            node: Node = stack.pop()
            res.append(node.val)

            if node.children:
                """reverse the order of children to iterate from left to right

                without it, last children in a level will be popped out of
                the stack first in line 33 above resulting in right -> left
                traversal
                """
                for ch in reversed(node.children):
                    stack.append(ch)

        return res
