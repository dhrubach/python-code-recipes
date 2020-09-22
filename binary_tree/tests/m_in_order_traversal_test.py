from binary_tree.m_in_order_traversal import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_null_tree(self):
        bt = BinaryTree()

        assert bt.inorderTraversalRecursive(None) == []
        assert bt.inorderTraversal(None) == []

    def test_lc_data_1(self):
        bt = BinaryTree()
        root = build([1, None, 2, None, None, 3, None])

        ans = bt.inorderTraversalRecursive(root)
        assert ans == [1, 3, 2]

        ans = bt.inorderTraversal(root)
        assert ans == [1, 3, 2]

    def test_lc_data_2(self):
        bt = BinaryTree()
        root = build([1])

        ans = bt.inorderTraversalRecursive(root)
        assert ans == [1]

        ans = bt.inorderTraversal(root)
        assert ans == [1]

    def test_lc_data_3(self):
        bt = BinaryTree()
        root = build([1, None, 2])

        ans = bt.inorderTraversalRecursive(root)
        assert ans == [1, 2]

        ans = bt.inorderTraversal(root)
        assert ans == [1, 2]
