#####################################################################################
# LeetCode Problem Number : 235
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
#####################################################################################
from binary_search_tree.tree_node import TreeNode


class BinarySearchTree:
    # runtime -> 78.79%, memory -> 10.5%
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        """The lowest common ancestor is defined between two nodes p and q
        as the lowest node in T that has both p and q as descendants
        (where we allow a node to be a descendant of itself)
        """
        if not root:
            return None

        while root:
            if root.val > p.val and root.val > q.val:
                """if the current root is greater than both the nodes,
                then go down left sub-tree to find LCA
                """
                root = root.left
            elif root.val < p.val and root.val < q.val:
                """if current root is less than both the nodes,
                then go down right sub-tree to find LCA
                """
                root = root.right
            else:
                """ current node is the LCA as it lies between the 2 nodes """
                break

        return root

    # runtime -> 97%, memory -> 10.64%
    def lowestCommonAncestorRecursive(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        if root.val > p.val and root.val > q.val:
            root = self.lowestCommonAncestorRecursive(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            root = self.lowestCommonAncestorRecursive(root.right, p, q)

        return root
