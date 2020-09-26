from binary_tree.m_post_order_traversal import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_null_tree(self):
        bt = BinaryTree()

        assert bt.postOrderRecursive(None) == []
        assert bt.postOrderIterative(None) == []
        assert bt.postOrderIterativeReverse(None) == []

    def test_lc_data_1(self):
        bt = BinaryTree()
        root = build([1, None, 2, None, None, 3, None])

        ans = bt.postOrderRecursive(root)
        assert ans == [3, 2, 1]

        ans = bt.postOrderIterative(root)
        assert ans == [3, 2, 1]

        ans = bt.postOrderIterativeReverse(root)
        assert ans == [3, 2, 1]

    def test_lc_data_2(self):
        bt = BinaryTree()
        root = build([1])

        ans = bt.postOrderRecursive(root)
        assert ans == [1]

        ans = bt.postOrderIterative(root)
        assert ans == [1]

        ans = bt.postOrderIterativeReverse(root)
        assert ans == [1]

    def test_lc_data_3(self):
        bt = BinaryTree()
        root = build([3, 9, 20, 4, 5, 15, 7, 2, 1, None, None, None, None, None, None])

        ans = bt.postOrderRecursive(root)
        assert ans == [2, 1, 4, 5, 9, 15, 7, 20, 3]

        ans = bt.postOrderIterative(root)
        assert ans == [2, 1, 4, 5, 9, 15, 7, 20, 3]

        ans = bt.postOrderIterativeReverse(root)
        assert ans == [2, 1, 4, 5, 9, 15, 7, 20, 3]
