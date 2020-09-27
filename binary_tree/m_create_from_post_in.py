###############################################################################################
# LeetCode Problem Number : 106
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
################################################################################################
from binary_search_tree.tree_node import TreeNode
from typing import List


class BinaryTree:
    # runtime -> 53.78%, memory -> 30.35%
    def buildFromPostInOrder(
        self, postorder: List[int], inorder: List[int]
    ) -> TreeNode:
        """ use post-order to fetch the nodes
            use in-order to build out the tree

            overall complexity of the algorithm : O(N^2)
               - searching for a value in in-order list : O(N) [line 35]
               - each recursive call : O(N) [line 40 & 41]
        """
        if not inorder or not postorder or len(inorder) == 0:
            return None

        """ last element of the post-order list is the current node
            each iteration will reduce the length of post-order list by 1

            since elements are popped from the end of the list, create
            right sub-tree followed by left sub-tree
        """
        cur = postorder.pop()
        node = TreeNode(cur)

        """ get the index of current node in in-order list """
        idx = inorder.index(cur)

        """ recursively build right and left sub-tree based on
            elements in in-order list
        """
        node.right = self.buildFromPostInOrder(postorder, inorder[idx + 1 :])
        node.left = self.buildFromPostInOrder(postorder, inorder[0:idx])

        return node

    # runtime -> 91.30%, memory -> 60.48%
    def buildFromPostInOrderWithMap(
        self, postorder: List[int], inorder: List[int]
    ) -> TreeNode:
        """ create a map of in-order list to replace
            O(N) search (when using 'index') to O(1)
        """
        map_inorder = {}
        for i, val in enumerate(inorder):
            map_inorder[val] = i

        """ instead of passing a modified in-order list
            to search for the index, use the map.

            `low` and `high` defines the sub-array inside
            in-order list
        """

        def build(low, high):
            if low > high:
                return None

            cur = TreeNode(postorder.pop())
            idx = map_inorder[cur.val]

            cur.right = build(idx + 1, high)
            cur.left = build(low, idx - 1)

            return cur

        """ nodes are range bound between 0 and number of nodes """
        return build(0, len(inorder) - 1)
