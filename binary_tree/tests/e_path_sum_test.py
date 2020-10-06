from binary_tree.e_path_sum import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_node_null(self):
        bt = BinaryTree()

        assert bt.hasPathSum(None, 0) is False

    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        root = build(nodes)

        ans = bt.hasPathSum(root, 22)
        assert ans is True

    def test_lc_data_2(self):
        bt = BinaryTree()
        nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
        root = build(nodes)

        ans = bt.hasPathSum(root, 27)
        assert ans is True
