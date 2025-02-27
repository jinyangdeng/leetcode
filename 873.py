"""
Original question: https://leetcode.com/problems/length-of-longest-fibonacci-subsequence
Very stingy about memory: Can't just use dp + memoization
"""

from typing import List
from collections import defaultdict


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        dp = {}

        for idx, num in enumerate(arr):
            dp[num] = defaultdict(lambda: 2)
            for i_1 in range(idx - 1, -1, -1):
                xi_1 = arr[i_1]
                xi = num - xi_1
                if xi >= xi_1:
                    break
                if xi not in dp:
                    continue
                dp[num][xi_1] = max(dp[num][xi_1], 1 + dp[xi_1][xi])
                res = max(res, dp[num][xi_1])

        return res
                