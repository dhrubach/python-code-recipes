from binary_tree.m_inform_employees import BinaryTree


class TestBinaryTree:
    def test_only_head(self):
        bt = BinaryTree()

        ans = bt.numOfMinutes(1, 0, [-1], [0])
        assert ans == 0

        ans = bt.numOfMinutesBFS(1, 0, [-1], [0])
        assert ans == 0

    def test_lc_data_1(self):
        bt = BinaryTree()

        ans = bt.numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0])
        assert ans == 1

        ans = bt.numOfMinutesBFS(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0])
        assert ans == 1

    def test_lc_data_2(self):
        bt = BinaryTree()

        ans = bt.numOfMinutes(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1])
        assert ans == 21

        ans = bt.numOfMinutesBFS(7, 6, [1, 2, 3, 4, 5, 6, -1], [0, 6, 5, 4, 3, 2, 1])
        assert ans == 21

    def test_lc_data_3(self):
        bt = BinaryTree()

        ans = bt.numOfMinutes(4, 2, [3, 3, -1, 2], [0, 0, 162, 914])
        assert ans == 1076

        ans = bt.numOfMinutesBFS(4, 2, [3, 3, -1, 2], [0, 0, 162, 914])
        assert ans == 1076

    def test_lc_data_4(self):
        bt = BinaryTree()

        ans = bt.numOfMinutes(
            15,
            0,
            [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        )
        assert ans == 3

        ans = bt.numOfMinutesBFS(
            15,
            0,
            [-1, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        )
        assert ans == 3

    def test_lc_data_5(self):
        bt = BinaryTree()

        ans = bt.numOfMinutes(
            11,
            4,
            [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
            [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337],
        )
        assert ans == 2560

        ans = bt.numOfMinutesBFS(
            11,
            4,
            [5, 9, 6, 10, -1, 8, 9, 1, 9, 3, 4],
            [0, 213, 0, 253, 686, 170, 975, 0, 261, 309, 337],
        )
        assert ans == 2560
