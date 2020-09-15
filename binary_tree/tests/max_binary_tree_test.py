from binary_tree.max_binary_tree import MaxBinaryTree


class TestMaxBinaryTree:
    def test_empty_tree(self):
        mbt = MaxBinaryTree()
        ans = mbt.construct([])

        assert ans is None

    def test_single_node(self):
        mbt = MaxBinaryTree()
        ans = mbt.construct([1])

        assert ans.val == 1
        assert ans.left is None
        assert ans.right is None

    def test_two_level(self):
        mbt = MaxBinaryTree()
        ans = mbt.construct([3, 5, 4])

        assert ans.val == 5
        assert ans.left.val == 3
        assert ans.right.val == 4

    def test_lc_data(self):
        mbt = MaxBinaryTree()
        ans = mbt.construct([3, 2, 1, 6, 0, 5])

        assert ans.val == 6
        assert ans.left.right.val == 2
        assert ans.right.val == 5
