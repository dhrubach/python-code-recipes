######################################################################
# LeetCode Problem Number : 700
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/search-in-a-binary-search-tree/
#####################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTreeCloneSearch:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        if cloned.val == target.val:
            return cloned

        return self.searchClonedNode(cloned, target.val)

    def searchClonedNode(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return None

        if node.val == val:
            return node

        found_node = self.searchClonedNode(node.left, val)
        if not found_node and node.right:
            found_node = self.searchClonedNode(node.right, val)

        return found_node

    def getTargetCopy_stack(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        # dfs
        stack = [cloned]

        while stack:
            node = stack.pop()

            if node.val == target.val:
                return node

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
