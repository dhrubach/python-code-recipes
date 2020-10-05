###########################################################################################
# LeetCode Problem Number : 1008
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
###########################################################################################
from binary_search_tree.tree_node import TreeNode
from typing import List


class BstFromPreOrder:
    # runtime -> 93.32%, memory -> 72.69%
    def create(self, preorder: List[int]) -> TreeNode:
        if not preorder or not len(preorder):
            return None

        """ return node for single element input """
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        """ in pre-order traversal, first element is the current node """
        root = TreeNode(preorder[0])

        """ insert all descendents of current node with val < root.val into left sub-array
            insert all descendents of current node with val > root.val into right sub-array
        """
        larr = []
        rarr = []
        for i in preorder[1:]:
            if i < root.val:
                larr.append(i)
            elif i > root.val:
                rarr.append(i)

        if len(larr):
            """ create left sub-tree of current node """
            root.left = self.create(larr)

        if len(rarr):
            """ create right sub-tree of current node """
            root.right = self.create(rarr)

        return root

    def create_inorder(self, preorder: List[int]) -> TreeNode:
        """sorting a pre-order traversal will give in-order traversal
        example :
            preorder -> [18, 9, 6, 3, 15, 12, 27, 24, 21, 30]
            inorder  -> [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        """
        inorder = sorted(preorder)

        return self.bst(preorder, inorder)

    def bst(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        if preorder:
            val = preorder.pop(0)
            root = TreeNode(val)

            """ find the position of current node in inorder array """
            idx = inorder.index(val)

            """ since inorder list is already sorted, all elements to
                the left of the list will form left sub-tree and all
                elements on the right will form right sub-tree
            """
            root.left = self.bst(preorder, inorder[:idx])
            root.right = self.bst(preorder, inorder[idx + 1 :])

            return root
