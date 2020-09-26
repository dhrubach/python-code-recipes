from binary_tree.m_pre_order_traversal import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_null_tree(self):
        bt = BinaryTree()

        assert bt.preOrderRecursive(None) == []
        assert bt.preOrderIterative(None) == []
        assert bt.preOrderIterativeSimple(None) == []

    def test_lc_data_1(self):
        bt = BinaryTree()
        root = build([1, None, 2, None, None, 3, None])

        ans = bt.preOrderRecursive(root)
        assert ans == [1, 2, 3]

        ans = bt.preOrderIterative(root)
        assert ans == [1, 2, 3]

        ans = bt.preOrderIterativeSimple(root)
        assert ans == [1, 2, 3]

    def test_lc_data_2(self):
        bt = BinaryTree()
        root = build([1])

        ans = bt.preOrderRecursive(root)
        assert ans == [1]

        ans = bt.preOrderIterative(root)
        assert ans == [1]

        ans = bt.preOrderIterativeSimple(root)
        assert ans == [1]

    def test_lc_data_3(self):
        bt = BinaryTree()
        root = build([3, 9, 20, 4, 5, 15, 7, 2, 1, None, None, None, None, None, None])

        ans = bt.preOrderRecursive(root)
        assert ans == [3, 9, 4, 2, 1, 5, 20, 15, 7]

        ans = bt.preOrderIterative(root)
        assert ans == [3, 9, 4, 2, 1, 5, 20, 15, 7]

        ans = bt.preOrderIterativeSimple(root)
        assert ans == [3, 9, 4, 2, 1, 5, 20, 15, 7]
