#####################################################################
# LeetCode Problem Number : 894
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/all-possible-full-binary-trees/
#####################################################################
from binary_search_tree.tree_node import TreeNode


class FullBinaryTree:
    """ A full binary tree is a binary tree where
        each node has exactly 0 or 2 child nodes

        number of nodes in a full binary tree is always an odd number
        each sub-tree is also a full binary tree
    """

    def __init__(self):
        """ store intermediate results for memoization """
        self.memo = {1: [TreeNode(0)]}

    # runtime -> 44.25%, memory -> 20.38%
    def findAllPossibleTrees(self, n: int) -> [TreeNode]:
        """ full binary tree cannot have even number of nodes """
        if n % 2 == 0:
            return []

        """ only root node for n = 1 """
        if n == 1:
            return [TreeNode(0)]

        res = []

        """ run the outer loop for only odd values till n

            number of nodes in left sub-tree : i
            number of nodes in right sub-tree : n - i - 1

            combine all possible left sub-trees with all possible
            right sub-trees to arrive at an answer
        """
        for i in range(1, n, 2):
            for left in self.findAllPossibleTrees(i):
                for right in self.findAllPossibleTrees(n - 1 - i):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res

    # runtime -> 77.25%, memory -> 64.88%
    def findAllPossibleTreesWithMemoization(self, n: int) -> [TreeNode]:
        """ full binary tree cannot have even number of nodes """
        if n % 2 == 0:
            return []

        if n not in self.memo:
            res = []

            """ run the outer loop for only odd values till n

                number of nodes in left sub-tree : i
                number of nodes in right sub-tree : n - i - 1

                combine all possible left sub-trees with all possible
                right sub-trees to arrive at an answer
            """
            for i in range(1, n, 2):
                for left in self.findAllPossibleTrees(i):
                    for right in self.findAllPossibleTrees(n - 1 - i):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)

            self.memo[n] = res

        return self.memo[n]
