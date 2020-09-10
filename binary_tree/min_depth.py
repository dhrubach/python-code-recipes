from binary_search_tree.tree_node import TreeNode


class BinaryTree:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return self.calculateDepth(root, 0)

    def calculateDepth(self, node: TreeNode, depth: int) -> int:
        if not node:
            return depth

        depth += 1

        ldepth = self.calculateDepth(node.left, 0) if node.left else None
        rdepth = self.calculateDepth(node.right, 0) if node.right else None

        if ldepth and rdepth:
            return depth + (ldepth if ldepth <= rdepth else rdepth)
        elif ldepth or rdepth:
            return depth + (ldepth or rdepth)
        else:
            return depth
