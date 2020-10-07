##################################################
# LeetCode Problem Number : 113
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/path-sum-ii/
##################################################
from binary_search_tree.tree_node import TreeNode
from typing import List


class BinaryTree:
    # runtime -> 61.20%, memory -> 15.95%
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        self.res = []

        def dfs(node: TreeNode, total: int, path: List[int]) -> List[List[int]]:
            if not node:
                return

            nonlocal sum

            if not node.left and not node.right and total == sum:
                self.res.append(path)

            if node.left:
                dfs(node.left, total + node.left.val, path + [node.left.val])

            if node.right:
                dfs(node.right, total + node.right.val, path + [node.right.val])

        dfs(root, root.val, [root.val])
        return self.res

    # runtime -> 93.70%, memory -> 67.41%
    def pathSumBFS(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = [(root, root.val, [root.val])]

        while queue:
            curr, val, ls = queue.pop(0)

            if not curr.left and not curr.right and val == sum:
                res.append(ls)

            if curr.left:
                queue.append((curr.left, val + curr.left.val, ls + [curr.left.val]))

            if curr.right:
                queue.append((curr.right, val + curr.right.val, ls + [curr.right.val]))

        return res
