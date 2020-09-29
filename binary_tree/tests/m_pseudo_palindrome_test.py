from binary_tree.m_pseudo_palindrome import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [2, 3, 1, 3, 1, None, 1]
        root = build(nodes)

        ans = bt.pseudoPalindromicPaths(root)
        assert ans == 2

    def test_lc_data_2(self):
        bt = BinaryTree()
        nodes = [2, 1, 1, 1, 3, None, None, None, None, None, 1]
        root = build(nodes)

        ans = bt.pseudoPalindromicPaths(root)
        assert ans == 1
