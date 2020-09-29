################################################################################
# LeetCode Problem Number : 1457
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
################################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # runtime -> 97.02%, memory -> 7.05%
    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        def dfs(root, count=0):
            if not root:
                return 0

            """ use an integer to keep track of the count of elements in each path from root to leaf.

                for each node value, shift 1 by those many bits and toggle the corresponding bit
                using a XOR gate. if a value has already been encountered before, then corresponding
                bit will be set to 0 else 1

                initial count : 0000
                node val : 2
                shift 1 by (node.val - 1) digits -> 1 << 1 -> 0010
                flip the second bit -> 0000 ^ 0010 -> 0010

                on encountering 2 again lower down the path, 2nd bit
                will be flipped to 0 indicating an even number of '2's
                in the path

                initial count : 0010
                flip the second bit -> 0010 ^ 0010 -> 0000
            """
            count ^= 1 << (root.val - 1)

            res = dfs(root.left, count) + dfs(root.right, count)

            if root.left == root.right:
                """if count has only 1 set bit, then that would be a power of 2 and count-1 would be the previous number,
                which would have all the bits that are less significant (bits towards the right) to the set bit will be set.
                Performing an & operation will result in 0

                Example -> Let's take the count represented by 8 bits, and has a value: 16 ->00010000.
                Now, count-1 would be: 15 ->00001111.
                Performing an & would result in 0
                """
                if count & (count - 1) == 0:
                    res += 1

            return res

        return dfs(root)
