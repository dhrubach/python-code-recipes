########################################################
# LeetCode Problem Number : 200
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/number-of-islands/
########################################################
from typing import List


class NumberOfIslands:
    def calculate(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    """start a search once you encounter a '1'

                    increment counter by 1 upon return
                    """
                    self.dfs_search(grid, i, j)
                    count += 1

        return count

    # runtime -> 81.74%, memory -> 78.79%
    def dfs_search(self, grid: List[List[int]], i: int, j: int) -> None:
        """base condition : if current cell position is out of grid or
        refers to a '0', then return
        """
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
            return

        """ mark a cell as visited """
        grid[i][j] = "#"

        """ navigate to all 4 directions around a cell """
        self.dfs_search(grid, i + 1, j)
        self.dfs_search(grid, i - 1, j)
        self.dfs_search(grid, i, j + 1)
        self.dfs_search(grid, i, j - 1)
