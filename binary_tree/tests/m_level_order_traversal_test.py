from binary_tree.m_level_order_traversal import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_null_tree(self):
        bt = BinaryTree()
        ans = bt.levelOrder(None)

        assert ans == []

    def test_single_node(self):
        bt = BinaryTree()
        nodes = [1]
        root = build(nodes)

        ans = bt.levelOrder(root)
        assert ans == [[1]]

    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [3, 9, 20, None, None, 15, 7]
        root = build(nodes)

        ans = bt.levelOrder(root)
        assert ans[1] == [9, 20]
        assert ans[2] == [15, 7]
