"""
Original question: https://leetcode.com/problems/sequential-grid-path-cover
To simplify there could have 2 improvements:
1. Externalise the path instead of keeping it as a function parameter and returning it. Just operate on the path in the backtrack function
2. Modify the cell, e.g. change to -1, to mark it as used
"""

from typing import List
from itertools import product

class Solution:
    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        def backtrack(i, j, _k, visited):
            if len(visited) == m * n:
                return visited

            for di, dj in [[0, -1], [0, 1], [-1, 0], [1, 0]]:
                newi, newj = i + di, j + dj
                if not (0 <= newi < m and 0 <= newj < n):
                    continue
                if [newi, newj] in visited:
                    continue
                if grid[newi][newj] not in (0, _k + 1):
                    continue
                visited.append([newi, newj])
                res = backtrack(newi, newj, max(_k, grid[newi][newj]),visited)
                if len(res) == m * n:
                    return res
                visited.pop()

            return visited

        for i, j in product(range(m), range(n)):
            if grid[i][j] > 1:
                continue
            res = backtrack(i, j, grid[i][j], [[i, j]])
            if len(res) == m * n:
                return res

        return []