from binary_tree.min_depth import BinaryTree
from binarytree import build


class TestMinDeptBinaryTree:
    def test_null_input(self):
        bt = BinaryTree()

        ans = bt.minDepth(None)
        assert ans == 0

    def test_root_node(self):
        bt = BinaryTree()
        nodes = [1]
        rt = build(nodes)

        ans = bt.minDepth(rt)
        assert ans == 1

    def test_single_child(self):
        bt = BinaryTree()
        nodes = [1, 2, None]
        rt = build(nodes)

        ans = bt.minDepth(rt)
        assert ans == 2

    def test_line_tree(self):
        bt = BinaryTree()
        nodes = [
            1,
            2,
            None,
            3,
            None,
            None,
            None,
            4,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ]
        rt = build(nodes)

        ans = bt.minDepth(rt)
        assert ans == 4

        nodes = [
            1,
            None,
            2,
            None,
            None,
            None,
            3,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            4,
        ]
        rt = build(nodes)

        ans = bt.minDepth(rt)
        assert ans == 4

    def test_lc_data(self):
        bt = BinaryTree()
        nodes = [3, 9, 20, None, None, 15, 7]
        rt = build(nodes)

        ans = bt.minDepth(rt)
        assert ans == 2

        nodes = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13]
        rt = build(nodes)

        ans = bt.minDepth(rt)
        assert ans == 3

    def test_line_tree_bfs(self):
        bt = BinaryTree()
        nodes = [
            1,
            2,
            None,
            3,
            None,
            None,
            None,
            4,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ]
        rt = build(nodes)

        ans = bt.minDepth_bfs(rt)
        assert ans == 4

        nodes = [
            1,
            None,
            2,
            None,
            None,
            None,
            3,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            4,
        ]
        rt = build(nodes)

        ans = bt.minDepth_bfs(rt)
        assert ans == 4

    def test_lc_data_bfs(self):
        bt = BinaryTree()
        nodes = [3, 9, 20, None, None, 15, 7]
        rt = build(nodes)

        ans = bt.minDepth_bfs(rt)
        assert ans == 2

        nodes = [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13]
        rt = build(nodes)

        ans = bt.minDepth_bfs(rt)
        assert ans == 3
