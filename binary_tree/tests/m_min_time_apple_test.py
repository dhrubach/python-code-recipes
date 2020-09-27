from binary_tree.m_min_time_apple import BinaryTree


class TestBinaryTree:
    def test_null_node(self):
        bt = BinaryTree()

        assert bt.minTimeTree(n=1, edges=[[0, 0]], hasApple=[True]) == 0
        assert bt.minTimeGraph(n=1, edges=[[0, 0]], hasApple=[True]) == 0

    def test_lc_data_1(self):
        bt = BinaryTree()
        n = 7
        edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
        hasApple = [False, False, True, False, True, True, False]

        assert bt.minTimeTree(n, edges, hasApple) == 8
        assert bt.minTimeGraph(n, edges, hasApple) == 8

    def test_lc_data_2(self):
        bt = BinaryTree()
        n = 4
        edges = [[0, 2], [0, 3], [1, 2]]
        hasApple = [False, True, False, False]

        assert bt.minTimeTree(n, edges, hasApple) == 0
        assert bt.minTimeGraph(n, edges, hasApple) == 4
