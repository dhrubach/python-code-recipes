from depth_first_search.m_number_of_islands import NumberOfIslands


class TestNumberOfIslands:
    def test_empty_grid(self):
        nm = NumberOfIslands()
        ans = nm.calculate(None, "dfs")

        assert ans == 0

    def test_single_island(self):
        nm = NumberOfIslands()

        ans = nm.calculate([[1]], "dfs")
        assert ans == 1

        ans = nm.calculate([[1]], "bfs")
        assert ans == 1

    def test_no_island(self):
        nm = NumberOfIslands()

        ans = nm.calculate([[0]], "dfs")
        assert ans == 0

        ans = nm.calculate([[0]], "bfs")
        assert ans == 0

    def test_lc_input_1(self):
        nm = NumberOfIslands()

        grid = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        ans = nm.calculate(grid, "dfs")
        assert ans == 1

        grid = [
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        ans = nm.calculate(grid, "bfs")
        assert ans == 1

    def test_lc_input_2(self):
        nm = NumberOfIslands()

        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        ans = nm.calculate(grid, "dfs")
        assert ans == 3

        grid = [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 1],
        ]
        ans = nm.calculate(grid, "bfs")
        assert ans == 3
