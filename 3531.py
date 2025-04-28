"""
Original question: https://leetcode.com/problems/count-covered-buildings
"""

from typing import List
from collections import defaultdict

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        x_ranges = defaultdict(lambda: [float('inf'), float('-inf')])
        y_ranges = defaultdict(lambda: [float('inf'), float('-inf')])

        for x, y in buildings:
            x_ranges[x][0] = min(x_ranges[x][0], y)
            x_ranges[x][1] = max(x_ranges[x][1], y)
            y_ranges[y][0] = min(y_ranges[y][0], x)
            y_ranges[y][1] = max(y_ranges[y][1], x)

        return sum(
            x_ranges[x][0] < y < x_ranges[x][1] and y_ranges[y][0] < x < y_ranges[y][1]
            for x, y in buildings
        )