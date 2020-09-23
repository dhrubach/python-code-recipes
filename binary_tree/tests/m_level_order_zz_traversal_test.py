from binary_tree.m_level_order_zz_traversal import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_null_tree(self):
        bt = BinaryTree()
        ans = bt.zigzagLevelOrder(None)

        assert ans == []

    def test_single_node(self):
        bt = BinaryTree()
        nodes = [1]
        root = build(nodes)

        ans = bt.zigzagLevelOrder(root)
        assert ans == [[1]]

    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [3, 9, 20, None, None, 15, 7]
        root = build(nodes)

        ans = bt.zigzagLevelOrder(root)
        assert ans[1] == [20, 9]
        assert ans[2] == [15, 7]

    def test_lc_data_2(self):
        bt = BinaryTree()
        nodes = [1, 2, 3, 4, None, None, 5]
        root = build(nodes)

        ans = bt.zigzagLevelOrder(root)
        assert ans[1] == [3, 2]
        assert ans[2] == [4, 5]

    def test_lc_data_3(self):
        bt = BinaryTree()
        nodes = [0, 2, 4, 1, None, 3, -1, 5, 1, None, None, None, 6, None, 8]
        root = build(nodes)

        ans = bt.zigzagLevelOrder(root)
        assert len(ans) == 4
        assert ans[3] == [8, 6, 1, 5]

    def test_lc_data_4(self):
        bt = BinaryTree()
        nodes = [1, 2]
        root = build(nodes)

        ans = bt.zigzagLevelOrder(root)
        assert len(ans) == 2
        assert ans[1] == [2]
