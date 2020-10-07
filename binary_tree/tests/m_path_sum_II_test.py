from binary_tree.m_path_sum_II import BinaryTree
from binarytree import build


class TestBinaryTree:
    def test_lc_data_1(self):
        bt = BinaryTree()
        nodes = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]
        root = build(nodes)

        ans = bt.pathSum(root, 22)
        assert len(ans) == 2
        assert ans[0] == [5, 4, 11, 2]

        ans = bt.pathSumBFS(root, 22)
        assert len(ans) == 2
        assert ans[1] == [5, 8, 4, 5]

    def test_null_node(self):
        bt = BinaryTree()

        ans = bt.pathSum(None, 0)
        assert ans == []

        ans = bt.pathSumBFS(None, 0)
        assert ans == []
