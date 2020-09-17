from binary_search_tree.e_search_bst import BinarySearchTree
from binarytree import build


class TestBinarySearchTree:
    def test_null_node(self):
        bst = BinarySearchTree()
        ans = bst.searchBST(None, 10)

        assert ans is None

    def test_root_node(self):
        bst = BinarySearchTree()
        nodes = [4]
        ip = build(nodes)

        ans = bst.searchBST(ip, 4)

        assert ans == ip

    def test_small_tree(self):
        bst = BinarySearchTree()
        nodes = [4, 2, 7, 1, 3]
        ip = build(nodes)

        ans = bst.searchBST(ip, 2)

        assert ans.left.val == 1

    def test_large_tree(self):
        bst = BinarySearchTree()
        nodes = [18, 9, 27, 6, 15, 24, 30, 3, None, 12, None, 21]
        ip = build(nodes)

        ans = bst.searchBST(ip, 24)

        assert ans.left.val == 21

    def test_fail_search(self):
        bst = BinarySearchTree()
        nodes = [4, 2, 7, 1, 3]
        ip = build(nodes)

        ans = bst.searchBST(ip, 5)

        assert ans is None
