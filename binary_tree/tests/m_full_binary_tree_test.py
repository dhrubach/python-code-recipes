from binary_tree.m_full_binary_tree import FullBinaryTree


class TestFullBinaryTree:
    def test_single_node(self):
        fbt = FullBinaryTree()
        ans = fbt.findAllPossibleTrees(1)

        assert len(ans) == 1
        assert ans[0].left is None
        assert ans[0].val == 0
        assert ans[0].right is None

    def test_lc_data(self):
        fbt = FullBinaryTree()

        ans = fbt.findAllPossibleTrees(7)
        assert len(ans) == 5

        ans = fbt.findAllPossibleTreesWithMemoization(7)
        assert len(ans) == 5
