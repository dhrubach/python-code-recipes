######################################################################
# LeetCode Problem Number : 145
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/binary-tree-postorder-traversal/
######################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # runtime -> 78.57%, memory -> 5.16%
    def preOrderRecursive(self, root: TreeNode) -> [int]:
        if not root:
            return []

        res = []

        """ pre - order traversal

            visit node
            visit left sub - tree
            visit right sub - tree
        """
        res.append(root.val)
        res += self.preOrderRecursive(root.left)
        res += self.preOrderRecursive(root.right)

        return res

    # runtime -> 93.15%, memory -> 8.86%
    def preOrderIterative(self, root: TreeNode) -> [int]:
        if not root:
            return []

        res = []

        """ on visiting a node, push 2 copies to the stack.

            use 1st copy to insert into result
            use 2nd copy to process the child nodes
        """
        stack = [root] * 2

        while stack:
            node = stack.pop()

            if stack and stack[-1] is node:
                res.append(node.val)
            else:
                """ insert right child node followed by left

                    this ensures processing is done from left to right
                """
                if node.right:
                    stack += [node.right] * 2
                if node.left:
                    stack += [node.left] * 2

        return res

    def preOrderIterativeSimple(self, root: TreeNode) -> [int]:
        if not root:
            return []

        res, stack = [], [root]

        while stack:
            cur = stack.pop()

            if cur:
                res.append(cur.val)
                stack.append(cur.right)
                stack.append(cur.left)

        return res
