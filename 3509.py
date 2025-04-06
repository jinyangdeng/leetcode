"""
Original question: https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        if abs(k) > sum(nums):
            return -1
        N = 2 * sum(nums) + 1 # Account for negative, 0, positive
        MID = N // 2 # Position of 0
        prev = [[set(), set()] for i in range(N)]

        for num in nums:
            new = [[set(), set()] for i in range(N)]
            for i in range(N - 1, -1, -1):
                for j in range(2):
                    for p in prev[i][j]:
                        if j == 0:
                            new[i - num][1].add(min(p * num, limit + 1))
                            new[i][0].add(p)
                        else:
                            new[i + num][0].add(min(p * num, limit + 1))
                            new[i][1].add(p)
            new[MID + num][0].add(min(num, limit + 1))
            prev = new

        res = prev[MID + k][0].union(prev[MID + k][1])
        res = [num for num in res if num <= limit]
        if len(res) == 0:
            return -1
        return max(res)
                