from binary_tree.m_find_elements import FindElements
from binary_search_tree.tree_node import TreeNode


class TestFindElements:
    def test_lc_data_1(self):
        root = TreeNode(-1, left=None, right=TreeNode(-1))
        fe = FindElements(root)

        assert fe.root.val == 0
        assert fe.root.right.val == 2
        assert fe.find_bit(1) is False
        assert fe.find_bit(2) is True

    def test_lc_data_2(self):
        root = TreeNode(
            -1,
            left=TreeNode(-1, left=TreeNode(-1), right=TreeNode(-1)),
            right=TreeNode(-1),
        )
        fe = FindElements(root)

        assert fe.find(1) is True
        assert fe.find(3) is True
        assert fe.find(5) is False

    def test_lc_data_3(self):
        root = TreeNode(
            -1, left=None, right=TreeNode(-1, left=TreeNode(-1, left=TreeNode(-1)))
        )
        fe = FindElements(root)

        assert fe.find(2) is True
        assert fe.find(3) is False
        assert fe.find(4) is False
        assert fe.find(5) is True
