"""
Original question: https://leetcode.com/problems/shortest-common-supersequence
It will be too memory-intensive to memoise both the length and actual string.
Hence, I memoise the length only, and reconstruct the actual string later.
"""

from functools import lru_cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)

        @lru_cache(maxsize=None)
        def dp(i, j):
            if i == N and j == M:
                return 0
            if i == N:
                return M - j
            if j == M:
                return N - i
            if str1[i] == str2[j]:
                return 1 + dp(i + 1, j + 1)
            return min(1 + dp(i + 1, j), 1 + dp(i, j + 1))

        target = dp(0, 0)
        res = ""
        i, j = 0, 0
        while i < N and j < M:
            if str1[i] == str2[j]:
                target -= 1
                res += str1[i]
                i += 1
                j += 1
                continue
            if dp(i + 1, j) == target - 1:
                target -= 1
                res += str1[i]
                i += 1
            elif dp(i, j + 1) == target - 1:
                target -= 1
                res += str2[j]
                j += 1
        
        if i < N:
            res += str1[i:]
        if j < M:
            res += str2[j:]

        return res