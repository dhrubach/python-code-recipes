##############################################################################
# LeetCode Problem Number : 1305
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/all-elements-in-two-binary-search-trees/
##############################################################################
from binary_search_tree.tree_node import TreeNode


class BinarySearchTree:
    # runtime -> 23.20%, memory -> 54.83%
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> [int]:
        if not root1 and not root2:
            return []

        if not root1:
            return sorted(self.generateElement(root2))

        if not root2:
            return sorted(self.generateElement(root1))

        arr = self.generateElement(root1)
        arr += self.generateElement(root2)
        return sorted(arr)

    def generateElement(self, root: TreeNode) -> [int]:
        if not root:
            return []

        if not root.left and not root.right:
            return [root.val]

        arr = [root.val]

        if root.left:
            arr += self.generateElement(root.left)
        if root.right:
            arr += self.generateElement(root.right)

        return arr

    # runtime -> 91.53%, memory -> 17.58%
    def getAllElements_dfs(self, root1: TreeNode, root2: TreeNode) -> [int]:
        output = []

        def dfs(node):
            nonlocal output
            if not node:
                return
            dfs(node.left)
            output.append(node.val)
            dfs(node.right)

        dfs(root1)
        dfs(root2)

        output.sort()
        return output
