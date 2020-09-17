#####################################################################
# LeetCode Problem Number : 590
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/n-ary-tree-postorder-traversal/
#####################################################################
from binary_tree.node import Node


class PostorderTreeTraversal:
    def traverse(self, root: Node) -> [int]:
        if not root:
            return []

        """ create an empty list to record elements under a sub-tree """
        res = []

        """ check for leaf node """
        if root.children:
            for ch in root.children:
                """ for each child node, traverse its sub-tree """
                res += self.traverse(ch)

        """ record a node post processing all child nodes """
        res.append(root.val)

        """ return traversed nodes of a sub-tree """
        return res

    def traverse_iterative(self, root: Node) -> [int]:
        if not root:
            return []

        # DFS
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.children:
                stack += [child for child in node.children]

        """ since nodes are visited in the following order :
                root -> right subtree -> left substree

            reverse the list to get the post-order traversal
        """
        return list(reversed(res))
