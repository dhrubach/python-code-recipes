from binary_tree.m_lowest_common_ancestor import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = build(nodes)

        ans = bt.lowestCommonAncestorParentMap(root, root.left, root.right)
        assert ans.val == 3

        ans = bt.lowestCommonAncestorRecursive(root, root.left, root.right)
        assert ans.val == 3

    def test_lc_data_2(self):
        bt = BinaryTree()
        nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
        root = build(nodes)

        ans = bt.lowestCommonAncestorParentMap(root, root.left, root.left.right.left)
        assert ans.val == 5

        ans = bt.lowestCommonAncestorRecursive(
            root, root.left.left, root.left.right.left
        )
        assert ans.val == 5
