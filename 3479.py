"""
Original question: https://leetcode.com/problems/fruits-into-baskets-iii
Trick: I cannot just 2 * N, but must 2 * math.ceil(math.log2(len(values)))
This is because if I just 2 * N

1(x) -----
 |       |
2(x) --------------
 |       |        |
 |     (3)x      4(x)
 |     |  |      |  |
(5)x (6)x (7)x (8)x (9)x

When I am at (2)x, I will think that (4)x is more left than (5)x, and give it preference.

"""
import math
from typing import List


class SegmentTree:
    def __init__(self, values):
        self.N = 2 ** math.ceil(math.log2(len(values)))
        self.values = [0] * 2 * self.N
        for idx, val in enumerate(values):
            self.update(self.N + idx, val)

    def update(self, idx, val):
        self.values[idx] = val
        while idx > 1:
            self.values[idx // 2] = max(self.values[idx], self.values[idx ^ 1])
            idx = idx // 2

    def query(self, target):
        if self.values[1] < target:
            return - 1
        idx = 1
        while idx < self.N:
            if self.values[idx * 2] >= target:
                idx = idx * 2
            else:
                idx = idx * 2 + 1
        return idx


class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        segmentTree = SegmentTree(baskets)

        res = 0
        for f in fruits:
            idx = segmentTree.query(f)
            if idx == -1:
                res += 1
            else:
                segmentTree.update(idx, -1)
        return res
