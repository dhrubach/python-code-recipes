from binary_tree.m_max_binary_tree_insert import MaxBinaryTree
from binary_search_tree.tree_node import TreeNode


class TestMaxBinaryTree:
    def test_null_node(self):
        mbt = MaxBinaryTree()
        ans = mbt.construct(None, 3)

        assert ans.val == 3

    def test_single_node(self):
        mbt = MaxBinaryTree()
        ans = mbt.construct(TreeNode(4), 5)

        assert ans.val == 5
        assert ans.left.val == 4

    def test_lc_data(self):
        mbt = MaxBinaryTree()
        max_tree = TreeNode(5, left=TreeNode(2, right=TreeNode(1)), right=TreeNode(4))
        ans = mbt.construct(max_tree, 3)

        assert ans.right.right.val == 3

        max_tree = TreeNode(5, left=TreeNode(2, right=TreeNode(1)), right=TreeNode(3))
        ans = mbt.construct(max_tree, 4)

        assert ans.right.val == 4
