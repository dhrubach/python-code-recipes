from binary_tree.m_sum_root_to_leaf import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_null_tree(self):
        bt = BinaryTree()
        assert bt.sumNumbers(None) == 0

    def test_lc_Data_1(self):
        bt = BinaryTree()
        nodes = [1, 2, 3]
        root = build(nodes)

        ans = bt.sumNumbers(root)
        assert ans == 25

    def test_lc_Data_2(self):
        bt = BinaryTree()
        nodes = [4, 9, 0, 5, 1, None, None]
        root = build(nodes)

        ans = bt.sumNumbers(root)
        assert ans == 1026
