###################################################################
# LeetCode Problem Number : 1315
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/flip-equivalent-binary-trees/
###################################################################
from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    # DFS - iterative
    def flipEquivalent(self, root1: TreeNode, root2: TreeNode) -> bool:
        stack1 = [root1]
        stack2 = [root2]

        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()

            if node1 is None and node2 is None:
                continue
            elif not node1 or not node2 or node1.val != node2.val:
                return False

            ln = (
                node1.left.val if node1.left is not None else -1,
                node1.right.val if node1.right is not None else -1,
            )
            rn = (
                node2.left.val if node2.left is not None else -1,
                node2.right.val if node2.right is not None else -1,
            )

            """ if nodes are same, then read child nodes of 1st tree in order,
                else reverse order of child nodes
            """
            if ln[0] == rn[0] and ln[1] == rn[1]:
                stack1.extend([node1.left, node1.right])
            else:
                stack1.extend([node1.right, node1.left])
            stack2.extend([node2.left, node2.right])

        return not stack1 and not stack2

    # runtime -> 97.18%, memory -> 38.48%
    def flipEquivalent_recursive(self, root1, root2):
        """ if both nodes are empty (child of leaf nodes or empty nodes), those are equivalent  """
        if root1 is None and root2 is None:
            return True

        """ if either node is empty, then nodes are not equivalent """
        if root1 is None or root2 is None:
            return False

        """ if values do not match, then nodes are not equivalent """
        if root1.val != root2.val:
            return False

        """ primary evaluating condition:
                left and right sub-trees of both nodes are same
                OR
                    left sub-tree of 1st node == right sub-tree of 2nd node
                    AND
                    right sub-tree of 1st node == left sub-tree of 2nd node
        """
        return (
            self.flipEquivalent_recursive(root1.left, root2.left)
            and self.flipEquivalent_recursive(root1.right, root2.right)
        ) or (
            self.flipEquivalent_recursive(root1.right, root2.left)
            and self.flipEquivalent_recursive(root1.left, root2.right)
        )
