#############################################################
# LeetCode Problem Number : 998
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/maximum-binary-tree-ii/
#############################################################
from binary_search_tree.tree_node import TreeNode


class MaxBinaryTree:
    """ Given root node of a maximum binary tree and a value,
        construct a new binary tree with the input value appended
        to the original binary tree
    """

    def construct(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        """ if val is greater than current root node, then
            make it the new root node. Assign current root
            node as left sub-tree of new root node

            example : input : [1,4,2,3]
                      val : 5
                      output : [1,4,2,3,5] -> 5 is the new root node
        """
        if val > root.val:
            root = TreeNode(val, left=root)
        else:
            """ push the new value to the right sub-tree of
                current node

                example : input : [2,1,5,3]
                          val : 4
                          output : [2,1,5,3,4]
                            -> 5 is the root node
                            -> 4 is the first child node of right sub-tree
            """
            root.right = self.construct(root.right, val)

        return root
