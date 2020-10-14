from depth_first_search.m_surrounded_regions import SurroundedRegions


class TestSurroundedRegions:
    def test_none_board(self):
        sr = SurroundedRegions()

        assert sr.calculate(None) is None

    def test_single_board(self):
        sr = SurroundedRegions()

        ans = sr.calculate([["X"]])
        assert ans == [["X"]]

        ans = sr.calculate([["O"]])
        assert ans == [["O"]]

    def test_lc_data_1(self):
        sr = SurroundedRegions()

        ans = sr.calculate([["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]])
        assert ans == [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

    def test_lc_data_2(self):
        sr = SurroundedRegions()

        ans = sr.calculate(
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ]
        )

        return_board = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]

        assert ans == return_board

    def test_lc_data_3(self):
        sr = SurroundedRegions()

        ans = sr.calculate([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])

        return_board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

        assert ans == return_board

    def test_lc_data_4(self):
        sr = SurroundedRegions()

        ans = sr.calculate(
            [
                ["O", "X", "X", "O", "X"],
                ["X", "O", "O", "X", "O"],
                ["X", "O", "X", "O", "X"],
                ["O", "X", "O", "O", "O"],
                ["X", "X", "O", "X", "O"],
            ]
        )

        return_board = [
            ["O", "X", "X", "O", "X"],
            ["X", "X", "X", "X", "O"],
            ["X", "X", "X", "O", "X"],
            ["O", "X", "O", "O", "O"],
            ["X", "X", "O", "X", "O"],
        ]

        assert ans == return_board
