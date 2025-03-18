"""
Original question: https://leetcode.com/problems/closest-equal-element-queries
"""

from typing import List
from collections import defaultdict
import bisect


class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        N = len(nums)
        nums = nums + nums + nums

        positions = defaultdict(list)
        for idx, val in enumerate(nums):
            positions[val].append(idx)

        res = []
        for qIdx in queries:
            num = nums[N + qIdx]
            numIdx = bisect.bisect_left(positions[num], N + qIdx)
            prev = positions[num][numIdx - 1]
            nnext = positions[num][numIdx + 1]
            if prev == qIdx and nnext == 2 * N + qIdx:
                res.append(-1)
            else:
                res.append(min(abs(N + qIdx - prev), abs(N + qIdx - nnext)))
        return res
