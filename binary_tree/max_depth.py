#####################################################################
# LeetCode Problem Number : 104
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/maximum-depth-of-binary-tree/
#####################################################################

from binary_search_tree.tree_node import TreeNode
from collections import deque


class BinaryTree:

    # DFS -> runtime 40ms, memory 15.4MB
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            """ return 1 for leaf node """
            return 1
        elif not root.left:
            """if left child is not present, then calculate depth based only on right child

            add 1 for the current node
            """
            return 1 + self.maxDepth(root.right)
        elif not root.right:
            """if right child is not present, then calculate depth based only on left child

            add 1 for the current node
            """
            return 1 + self.maxDepth(root.left)
        else:
            """calculate depth of each child and return maximum of the two

            add 1 for the current node
            """
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # BFS -> runtime 40ms, memory 15MB
    def maxDepth_bfs(self, root: TreeNode) -> int:
        if not root:
            return 0

        """ depth at root level -> 1 """
        queue, level = deque([(root, 1)]), 0

        """ remove a node from beginning of the queue
            add a node to the end of the queue

            all nodes at a given level are processed from
            left to right in a single iteration
        """
        while queue:
            node, level = queue.popleft()

            if node.left:
                """if left node is present, add to queue

                increment level by 1 to reflect the child node level
                """
                queue.append((node.left, level + 1))

            if node.right:
                """if right node is present, add to queue

                increment level by 1 to reflect the child node level
                """
                queue.append((node.right, level + 1))

        """ level of the last popped node is the maximum tree depth """
        return level
