################################################################################
# LeetCode Problem Number : 1315
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
################################################################################
from binary_search_tree.tree_node import TreeNode


class FindElements:
    def __init__(self, root: TreeNode):
        self.seen = set()
        # self.root = self.dfs(root, 0)
        self.root = self.bfs(root)

    # runtime -> 78.49%, memory -> 14.14%
    def dfs(self, node: TreeNode, val: int) -> TreeNode:
        if not node:
            return

        node.val = val
        self.seen.add(val)
        if node.left:
            self.dfs(node.left, 2 * val + 1)
        if node.right:
            self.dfs(node.right, 2 * val + 2)

        return node

    # runtime -> 96.62%, memory -> 48.85%
    def dfs_optimized(self, node: TreeNode, val: int):
        self.seen.add(val)
        if node.left:
            self.dfs(node.left, 2 * val + 1)
        if node.right:
            self.dfs(node.right, 2 * val + 2)

    # runtime -> 89.40%, memory -> 5.07%
    def bfs(self, root: TreeNode) -> TreeNode:
        self.seen.add(0)
        stack = [(root, 0)]

        while stack:
            node, val = stack.pop()
            node.val = val

            if node.left:
                stack.append((node.left, 2 * val + 1))
                self.seen.add(2 * val + 1)

            if node.right:
                stack.append((node.right, 2 * val + 2))
                self.seen.add(2 * val + 2)

        return root

    def find(self, target: int) -> bool:
        return target in self.seen

    def find_bit(self, target: int) -> bool:
        binary = bin(target + 1)[3:]  # remove the useless first `1`
        index = 0
        root = self.root  # use a new pointer `root` to traverse the tree
        while root and index <= len(
            binary
        ):  # traverse the binary number from left to right
            if root.val == target:
                return True
            if binary[index] == "0":  # if it's 0, we have to go left
                root = root.left
            else:  # if it's 1, we have to go right
                root = root.right
            index += 1
        return False
