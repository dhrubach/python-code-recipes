########################################################
# LeetCode Problem Number : 200
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/number-of-islands/
########################################################
from typing import List, Deque
from collections import deque


class NumberOfIslands:
    def calculate(self, grid: List[List[int]], type: str) -> int:
        if not grid:
            return 0

        count = 0
        queue = deque([])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if type == "dfs":
                        """start a search once you encounter a '1'

                        increment counter by 1 upon return
                        """
                        self.dfs_search(grid, i, j)
                        count += 1
                    elif type == "bfs":
                        queue.append((i, j))
                        self.bfs_search(grid, queue)
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

    def bfs_search(self, grid: List[List[int]], queue: Deque) -> None:
        while queue:
            i, j = queue.popleft()
            grid[i][j] = "#"

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if (
                    x >= 0
                    and x < len(grid)
                    and y >= 0
                    and y < len(grid[0])
                    and grid[x][y] == 1
                ):
                    queue.append((x, y))
