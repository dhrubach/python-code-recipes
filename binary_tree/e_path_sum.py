###############################################
# LeetCode Problem Number : 112
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/path-sum/
###############################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        def dfs(node: TreeNode, total: int) -> bool:
            nonlocal sum
            res = False

            total += node.val

            if not node.left and not node.right:
                return total == sum

            if node.left:
                res = dfs(node.left, total)

            if node.right and not res:
                res = dfs(node.right, total)

            return res

        return dfs(root, 0)
