"""
Original question: https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings
Fairly standard kmp question with 2 interesting bits:
1. The last variable to avoid adding positions that had been added previously
2. Final translation from vertical index to horizon index, i.e. verticalAppears = set(i%m * n + i//m for i in verticalAppears)
"""

from typing import List

def lps(p):
    N = len(p)
    res = [0 for i in range(N)]
    j = 0
    for i in range(1, N):
        while j > 0 and p[i] != p[j]:
            j = res[j - 1]
        if p[i] == p[j]:
            j += 1
        res[i] = j
    return res

def getPattern(s, p):
    N = len(s)
    matches = []
    pat = lps(p)
    j = 0
    for i in range(N):
        while j > 0 and s[i] != p[j]:
            j = pat[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == len(p):
            j = pat[j - 1]
            matches.append(i - len(p) + 1)
    return matches

class Solution:
    def countCells(self, grid: List[List[str]], pattern: str) -> int:
        m, n = len(grid), len(grid[0])
        horizontalString = ''.join(char for row in grid for char in row)
        horizontalAppears = set()
        last = -1
        for startingPoint in getPattern(horizontalString, pattern):
            horizontalAppears.update(set(range(max(startingPoint, last), startingPoint + len(pattern))))
            last = startingPoint + len(pattern)

        verticalString = ''.join(grid[row][col] for col in range(n) for row in range(m))
        verticalAppears = set()
        last = -1
        for startingPoint in getPattern(verticalString, pattern):
            verticalAppears.update(set(range(max(startingPoint, last), startingPoint + len(pattern))))
            last = startingPoint + len(pattern)
        verticalAppears = set(i%m * n + i//m for i in verticalAppears)
        return len(horizontalAppears.intersection(verticalAppears))
        