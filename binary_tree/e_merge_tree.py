###############################################################
# LeetCode Problem Number : 617
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/merge-two-binary-trees/
###############################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTreeMerge:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        if not t1:
            return t2

        if not t2:
            return t1

        return self.createTree(t1, t2)

    def createTree(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        newNode = self.mergeNodes(t1, t2)

        if not newNode:
            return None

        newNode.left = self.createTree(t1.left if t1 else None, t2.left if t2 else None)
        newNode.right = self.createTree(
            t1.right if t1 else None, t2.right if t2 else None
        )

        return newNode

    def mergeNodes(self, t1: TreeNode, t2: TreeNode):
        if t1 and t2:
            return TreeNode(val=t1.val + t2.val)
        elif t1 or t2:
            return TreeNode(val=t1.val if t1 else t2.val)
        else:
            return None

    def mergeTrees_v2(self, t1: TreeNode, t2: TreeNode):
        if t1 and t2:
            return TreeNode(t1.val + t2.val,
                            self.mergeTrees_v2(t1.left, t2.left),
                            self.mergeTrees_v2(t1.right, t2.right))
        elif t1 or t2:
            return t1 or t2
        else:
            return None
