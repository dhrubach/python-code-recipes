#####################################################################
# LeetCode Problem Number : 111
# Difficulty Level : Easy
# URL : https://leetcode.com/problems/minimum-depth-of-binary-tree/
#####################################################################

from binary_search_tree.tree_node import TreeNode
from collections import deque


class BinaryTree:

    # DFS -> runtime 40ms, memory 15.8MB
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            """ return 1 for leaf node """
            return 1
        elif not root.left:
            """if left child is not present, then calculate depth based only on right child

            add 1 for the current node
            """
            return 1 + self.minDepth(root.right)
        elif not root.right:
            """if right child is not present, then calculate depth based only on left child

            add 1 for the current node
            """
            return 1 + self.minDepth(root.left)
        else:
            """calculate depth of each child and return minimum of the two

            add 1 for the current node
            """
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    # BFS -> runtime 40ms, memory 14.8MB
    def minDepth_bfs(self, root: TreeNode) -> int:
        if root is None:
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

            """ leaf node at a given level will be the minimum depth
            """
            if not node.left and not node.right:
                return level
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
