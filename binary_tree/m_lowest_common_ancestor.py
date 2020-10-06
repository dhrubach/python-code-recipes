##############################################################################
# LeetCode Problem Number : 236
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
##############################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # runtime -> 93.42%, memory -> 93.41%
    def lowestCommonAncestorParentMap(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """The lowest common ancestor is defined between two nodes p and q
        as the lowest node in T that has both p and q as descendants
        (where we allow a node to be a descendant of itself)
        """
        stack = [root]
        parent = {root: None}

        """ construct a map of each node to its parent """
        while p not in parent or q not in parent:
            node = stack.pop()

            if node.left:
                parent[node.left] = node
                stack.append(node.left)

            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        ancestors = set()

        """ create a path from p upto the root """
        while p:
            ancestors.add(p)
            p = parent[p]

        """ first node in q's ancestor path which is also in
            p's ancestor path is the answer
        """
        while q not in ancestors:
            ancestors.add(q)
            q = parent[q]

        return q

    # runtime -> 83.56%, memory -> 48.21%
    def lowestCommonAncestorRecursive(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestorRecursive(root.left, p, q)
        right = self.lowestCommonAncestorRecursive(root.right, p, q)

        """ if both p and q are found in the same sub-tree, then return current node.
            else return either p or q. Return None if neither nodes are present
            in the current sub-tree.
        """
        return root if left and right else left or right
