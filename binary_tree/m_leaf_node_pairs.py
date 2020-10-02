######################################################################
# LeetCode Problem Number : 1530
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
######################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    """ A pair of two different leaf nodes of a binary tree is said to be good
        if the length of the shortest path between them is less than or equal to distance.
    """

    # runtime -> 93.72%, memory -> 56.34%
    def countPairs(self, root: TreeNode, distance: int) -> int:
        count = 0

        def dfs(node):
            nonlocal count

            if not node:
                return []

            """ return 1 to parent if on a lead node """
            if not node.left and not node.right:
                return [1]

            """ post - order tree traversal

                left -> list of distances from current node down to
                        all possible leaf nodes in left sub-tree

                right -> list of distances from current node down to
                        all possible leaf nodes in right sub-tree
            """
            left = dfs(node.left)
            right = dfs(node.right)

            """ compute cartesian product of left and right lists

                if the total length between 2 leaf nodes is less than distance,
                then the pair is a good pair

                example : left : [1, 2], right : [1]
                          distance : 2
                          possible distances between leaf nodes : [2, 3]
                          only 1 combination meets the criteria
            """
            count += sum(l + r <= distance for l in left for r in right)

            """ when returning distances to parent, add 1 and then check
                for boundary condition

                example : left -> [1, 2], right -> [1]
                          possible leaf node distances from current node : d = [1, 2, 1]
                          distance : 3

                          return to parent : [d[0] + 1, d[2] + 1] -> [2 , 2]
            """
            return [n + 1 for n in left + right if n + 1 < distance]

        dfs(root)

        return count
