from binary_search_tree.m_k_smallest_element import BinarySearchTree
from binarytree import build


class TestBinarySearchTree:
    def test_lc_data_1(self):
        bst = BinarySearchTree()
        nodes = [3, 1, 4, None, 2, None, None]
        root = build(nodes)

        assert bst.kthSmallest(root, 1) == 1

    def test_lc_data_2(self):
        bst = BinarySearchTree()
        nodes = [5, 3, 6, 2, 4, None, None, 1, None, None, None]
        root = build(nodes)

        assert bst.kthSmallest(root, 3) == 3

    def test_lc_data_3(self):
        bst = BinarySearchTree()

        assert bst.kthSmallest(None, 1) == 0
