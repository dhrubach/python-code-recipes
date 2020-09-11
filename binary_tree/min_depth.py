#####################################################################
# LeetCode Problem Number : 111
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/minimum-depth-of-binary-tree/
#####################################################################

from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # DFS
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            """ return 1 for leaf node """
            return 1
        elif not root.left:
            """if left child is not present, then calculate depth based only on right child
            add 1 for the current node
            """
            return 1 + self.minDepth(root.right)
        elif not root.right:
            """if right child is not present, then calculate depth based only on left child
            add 1 for the current node
            """
            return 1 + self.minDepth(root.left)
        else:
            """calculate depth of each child and return minimum of the two
            add 1 for the current node
            """
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
