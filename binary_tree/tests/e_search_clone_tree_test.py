from binary_tree.e_search_clone_tree import BinaryTreeCloneSearch
from binary_search_tree.tree_node import TreeNode
from binarytree import build


class TestBinaryTreeCloneSearch:
    def test_single_node(self):
        btc = BinaryTreeCloneSearch()
        nodes = [7]
        bst = build(nodes)
        cloned_bst = build(nodes)

        ans = btc.getTargetCopy(bst, cloned_bst, TreeNode(7))

        assert ans.val == 7

    def test_lc_data_1(self):
        btc = BinaryTreeCloneSearch()
        nodes = [7, 4, 3, None, None, 6, 19]
        bst = build(nodes)
        cloned_bst = build(nodes)

        ans = btc.getTargetCopy(bst, cloned_bst, TreeNode(3))

        assert ans.val == 3

    def test_lc_data_2(self):
        btc = BinaryTreeCloneSearch()
        nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        bst = build(nodes)
        cloned_bst = build(nodes)

        ans = btc.getTargetCopy(bst, cloned_bst, TreeNode(5))

        assert ans.left.val == 10
