####################################################################
# LeetCode Problem Number : 94
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/binary-tree-inorder-traversal/
####################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # runtime -> 93.58%, memory -> 63.59%
    def inOrderIterative(self, root: TreeNode) -> [int]:
        res = []
        stack = []

        while root or stack:
            """ visit a node and record it into stack
                visit left child node, if one exists
            """
            while root:
                stack.append(root)
                root = root.left

            """ pop out last visited node
                insert the value into response list
                visit right child node, if one exists
            """
            root = stack.pop()
            res.append(root.val)
            root = root.right

        return res

    # runtime -> 93.58%, memory -> 63.59%
    def inOrderRecursive(self, root: TreeNode) -> [int]:
        if not root:
            return []

        res = []

        """ inorder traversal

            visit left sub-tree
            visit node
            visit right sub-tree
        """
        res += self.inOrderRecursive(root.left)
        res.append(root.val)
        res += self.inOrderRecursive(root.right)

        return res
