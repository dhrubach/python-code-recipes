from binary_tree.m_flip_binary_tree import BinaryTree
from binary_search_tree.tree_node import TreeNode
from binarytree import build


class TestBinaryTree:
    def test_null_roots(self):
        bt = BinaryTree()
        ans = bt.flipEquivalent(None, None)
        assert ans is True

        ans = bt.flipEquivalent_recursive(None, None)
        assert ans is True

    def test_single_root(self):
        bt = BinaryTree()

        ans = bt.flipEquivalent_recursive(TreeNode(1), None)
        assert ans is False

        ans = bt.flipEquivalent_recursive(TreeNode(1), None)
        assert ans is False

    def test_lc_data_1(self):
        bt = BinaryTree()

        ans = bt.flipEquivalent(
            TreeNode(0, right=TreeNode(1)), TreeNode(0, left=TreeNode(1))
        )
        assert ans is True

        ans = bt.flipEquivalent_recursive(
            TreeNode(0, right=TreeNode(1)), TreeNode(0, left=TreeNode(1))
        )
        assert ans is True

    def test_lc_data_2(self):
        bt = BinaryTree()
        root1 = TreeNode(
            1,
            left=TreeNode(
                2,
                left=TreeNode(4),
                right=TreeNode(5, left=TreeNode(7), right=TreeNode(8)),
            ),
            right=TreeNode(3, left=TreeNode(6)),
        )
        root2 = TreeNode(
            1,
            left=TreeNode(3, right=TreeNode(6)),
            right=TreeNode(
                2,
                left=TreeNode(4),
                right=TreeNode(5, left=TreeNode(8), right=TreeNode(7)),
            ),
        )

        ans = bt.flipEquivalent(root1, root2)
        assert ans is True

        ans = bt.flipEquivalent_recursive(root1, root2)
        assert ans is True

    def test_lc_data_3(self):
        bt = BinaryTree()
        root1 = build(
            [1, 3, 3, 4, 5, 6, None, None, None, 7, 8, None, None, None, None]
        )
        root2 = build([1, 3, 3, None, 6, 4, 5, None, None, None, None, 8, 7])

        ans = bt.flipEquivalent(root1, root2)
        assert ans is False

        ans = bt.flipEquivalent_recursive(root1, root2)
        assert ans is False
