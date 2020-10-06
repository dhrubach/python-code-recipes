from binary_search_tree.tree_node import TreeNode
from binary_search_tree.e_lowest_common_ancestor import BinarySearchTree
from binarytree import build


class TestBinarySearchTree:
    def test_lc_data_1(self):
        bst = BinarySearchTree()
        nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root = build(nodes)

        ans = bst.lowestCommonAncestor(root, TreeNode(2), TreeNode(8))
        assert ans.val == 6

        ans = bst.lowestCommonAncestorRecirsive(root, TreeNode(2), TreeNode(8))
        assert ans.val == 6

    def test_lc_data_2(self):
        bst = BinarySearchTree()
        nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root = build(nodes)

        ans = bst.lowestCommonAncestor(root, TreeNode(3), TreeNode(5))
        assert ans.val == 4

        ans = bst.lowestCommonAncestorRecirsive(root, TreeNode(3), TreeNode(5))
        assert ans.val == 4

    def test_lc_data_3(self):
        bst = BinarySearchTree()
        nodes = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
        root = build(nodes)

        ans = bst.lowestCommonAncestor(root, TreeNode(5), TreeNode(9))
        assert ans.val == 6

        ans = bst.lowestCommonAncestorRecirsive(root, TreeNode(5), TreeNode(9))
        assert ans.val == 6

    def test_null_root(self):
        bst = BinarySearchTree()
        assert bst.lowestCommonAncestor(None, None, None) is None
