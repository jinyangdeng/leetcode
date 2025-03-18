"""
Original question: https://leetcode.com/problems/zero-array-transformation-iv
"""
from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        MMAX = max(nums)
        dp = [[0] * (max(nums) + 1) for _ in range(N)]

        for idx, num in enumerate(nums):
            dp[idx][num] = 1

        if all(dp[i][0] == 1 for i in range(N)):
            return 0

        for idx, query in enumerate(queries):
            l, r, val = query
            for i in range(l, r + 1):
                for j in range(nums[i] - val + 1):
                    if dp[i][j + val] == 1:
                        dp[i][j] = 1

            if all(dp[i][0] == 1 for i in range(N)):
                return idx + 1

        return -1
