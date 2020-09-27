###############################################################################################
# LeetCode Problem Number : 105
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
################################################################################################
from binary_search_tree.tree_node import TreeNode
from typing import List


class BinaryTree:
    # runtime -> 55% memory --> 33.27%
    def buildFromPreInOrder(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """ use pre-order to fetch the nodes
            use in-order to build out the tree
        """
        if not preorder or not inorder or len(inorder) == 0:
            return None

        """ first element of the pre-order list is the current node
            each iteration will reduce the length of pre-order list by 1
        """
        cur = preorder.pop(0)
        node = TreeNode(cur)

        """ get the index of current node in in-order list """
        idx = inorder.index(cur)

        """ recursively build left and right sub-tree based on
            elements in in-order list
        """
        node.left = self.buildFromPreInOrder(preorder, inorder[:idx])
        node.right = self.buildFromPreInOrder(preorder, inorder[idx + 1 :])

        return node

    # runtime -> 97.56%, memory -> 82.56%
    def buildFromPreInOrderOptimized(
        self, preorder: List[int], inorder: List[int]
    ) -> TreeNode:
        def build(stop):
            if inorder and inorder[-1] != stop:
                root = TreeNode(preorder.pop())
                root.left = build(root.val)
                inorder.pop()
                root.right = build(stop)
                return root

        preorder.reverse()
        inorder.reverse()

        return build(None)
