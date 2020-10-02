from binary_tree.m_paths_city_zero import BinaryTree


class TestBinaryTree:
    def test_lc_data_1(self):
        bt = BinaryTree()
        connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]

        ans = bt.minReorder(6, connections)
        assert ans == 3

    def test_lc_data_2(self):
        bt = BinaryTree()
        connections = [[1, 0], [1, 2], [3, 2], [3, 4]]

        ans = bt.minReorder(5, connections)
        assert ans == 2

    def test_lc_data_3(self):
        bt = BinaryTree()
        connections = [[1, 0], [2, 0]]

        ans = bt.minReorder(3, connections)
        assert ans == 0
