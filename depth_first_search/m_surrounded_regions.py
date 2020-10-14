#########################################################
# LeetCode Problem Number : 130
# Difficulty Level : Medium
# URL : https://leetcode.com/problems/surrounded-regions/
#########################################################
from typing import List


class SurroundedRegions:
    # runtime -> 88.67%, memory -> 5.26%
    def calculate(self, board: List[List[int]]) -> List[List[int]]:
        if not board or len(board) == 0:
            return None

        r, c = len(board), len(board[0])
        for i in [0, r - 1]:
            for j in range(c):
                self.dfs_search(board, i, j)

        for i in range(r):
            for j in [0, c - 1]:
                self.dfs_search(board, i, j)

        for i in range(r):
            for j in range(c):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

        return board

    def dfs_search(self, board: List[List[int]], i: int, j: int) -> None:
        r, c = len(board), len(board[0])

        if 0 <= i < r and 0 <= j < c and board[i][j] == "O":
            board[i][j] = "T"

            self.dfs_search(board, i - 1, j)
            self.dfs_search(board, i + 1, j)
            self.dfs_search(board, i, j - 1)
            self.dfs_search(board, i, j + 1)
