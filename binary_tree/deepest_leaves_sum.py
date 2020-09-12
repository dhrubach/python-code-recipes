#########################################################
# LeetCode Problem Number : 1302
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/deepest-leaves-sum/
#########################################################
from binary_search_tree.tree_node import TreeNode
from collections import deque


class DeepestLeavesSum:
    # DFS --> runtime 44.62%, memory 88.59%
    def calculate(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return root.val

        max_level, total = -1, 0
        queue = deque([(root, 1)])

        while queue:
            node, level = queue.popleft()

            if not node.left and not node.right:
                """ when at a leaf node, add value to `total` when
                    at max depth
                """
                if level == max_level:
                    total += node.val

                """ if current level is higher than max_level, then
                    reset both `max_level` and `total`
                """
                if level > max_level:
                    max_level = level
                    total = node.val

            if node.left:
                queue.append((node.left, level + 1))

            if node.right:
                queue.append((node.right, level + 1))

        return total

    # runtime 65.59%, memory 83.38%
    def calculate_optimized(self, root: TreeNode) -> int:
        if not root:
            return 0

        cur_level = [root]
        next_level = []

        while cur_level:
            next_level = []

            """ at each level, insert child nodes to `next_level`
            """
            for node in cur_level:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)

            """ at maximum depth, leaf nodes will be copied into
                `next_level`. `cur_level` will be set to [].
            """
            next_level, cur_level = cur_level, next_level

        """ add the values of nodes to arrive at final result """
        return sum([x.val for x in next_level])
