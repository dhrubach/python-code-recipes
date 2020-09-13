################################################################################
# LeetCode Problem Number : 1315
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/
################################################################################
from binary_search_tree.tree_node import TreeNode
from collections import deque


class EvenGrandParent:
    # BFS runtime -> 21.74%, memory -> 17.55%
    def calculate(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, None, None)])
        total = 0

        while queue:
            curr, parent, gparent = queue.popleft()

            if gparent and gparent % 2 == 0:
                total += curr.val

            if curr.left:
                queue.append((curr.left, curr.val, parent or -1))
            if curr.right:
                queue.append((curr.right, curr.val, parent or -1))

        return total
