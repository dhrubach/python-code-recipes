from binary_search_tree.m_merge_bst_to_list import BinarySearchTree
from binary_search_tree.tree_node import TreeNode


class TestBinarySearchTree:
    def test_lc_data_1(self):
        root1 = TreeNode(2, left=TreeNode(1), right=TreeNode(4))
        root2 = TreeNode(1, left=TreeNode(0), right=TreeNode(3))

        bst = BinarySearchTree()
        ans = bst.getAllElements(root1, root2)
        assert len(ans) == 6
        assert ans[0] == 0

        ans = bst.getAllElements_dfs(root1, root2)
        assert len(ans) == 6
        assert ans[0] == 0

    def test_lc_data_2(self):
        root1 = TreeNode(0, left=TreeNode(-10), right=TreeNode(10))
        root2 = TreeNode(
            5, left=TreeNode(1, left=TreeNode(0), right=TreeNode(2)), right=TreeNode(7)
        )

        bst = BinarySearchTree()

        ans = bst.getAllElements(root1, root2)
        assert len(ans) == 8
        assert ans[-2] == 7

        ans = bst.getAllElements_dfs(root1, root2)
        assert len(ans) == 8
        assert ans[-2] == 7

    def test_lc_data_3(self):
        root1 = TreeNode(1, left=None, right=TreeNode(8))
        root2 = TreeNode(8, left=TreeNode(1), right=None)

        bst = BinarySearchTree()

        ans = bst.getAllElements(root1, root2)
        assert len(ans) == 4
        assert ans[0] == 1

        ans = bst.getAllElements_dfs(root1, root2)
        assert len(ans) == 4
        assert ans[0] == 1
