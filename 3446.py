"""
Original question: https://leetcode.com/problems/sort-matrix-by-diagonals
"""

from typing import List


class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        helper = []

        for startingColumn in range(n - 1, 0, -1):
            _range = n - startingColumn
            for i in range(_range):
                helper.append(grid[i][startingColumn + i])
            helper.sort()
            for i in range(_range):
                grid[i][startingColumn + i] = helper[i]
            helper.clear()

        for startingRow in range(0, n):
            _range = n - startingRow
            for i in range(_range):
                helper.append(grid[startingRow + i][i])
            helper.sort(reverse=True)
            for i in range(_range):
                grid[startingRow + i][i] = helper[i]
            helper.clear()

        return grid
