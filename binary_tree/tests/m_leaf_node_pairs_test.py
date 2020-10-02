from binary_tree.m_leaf_node_pairs import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [1, 2, 3, None, 4, None, None]
        root = build(nodes)

        ans = bt.countPairs(root, 3)
        assert ans == 1

    def test_lc_data_2(self):
        bt = BinaryTree()
        nodes = [1, 2, 3, 4, 5, 6, 7]
        root = build(nodes)

        ans = bt.countPairs(root, 3)
        assert ans == 2

    def test_lc_data_3(self):
        bt = BinaryTree()
        nodes = [7, 1, 4, 6, None, 5, 3, None, None, None, None, None, 2]
        root = build(nodes)

        ans = bt.countPairs(root, 3)
        assert ans == 1
