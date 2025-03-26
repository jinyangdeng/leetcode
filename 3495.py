"""
Original question: https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero
"""
from typing import List


class Solution:
    preComputed = [[1, 3, 1], [4, 15, 2], [16, 63, 3], [64, 255, 4], [256, 1023, 5], [1024, 4095, 6], [4096, 16383, 7],
                   [16384, 65535, 8], [65536, 262143, 9], [262144, 1048575, 10], [1048576, 4194303, 11],
                   [4194304, 16777215, 12], [16777216, 67108863, 13], [67108864, 268435455, 14],
                   [268435456, 1073741824, 15]]

    def calculate(self, query):
        res = 0

        for l, r, c in self.preComputed:
            if query[0] > r:
                continue
            if query[1] < l:
                break
            res += c * (min(query[1], r) - query[0] + 1)
            query[0] = r + 1
        return res // 2 + res % 2

    def minOperations(self, queries: List[List[int]]) -> int:
        return sum(self.calculate(q) for q in queries)
