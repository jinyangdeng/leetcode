"""
Original question: https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair
"""

from collections import Counter
from typing import List


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        helper = [[] for i in range(n + 1)]
        for idx, val in enumerate(conflictingPairs):
            # they may give [10, 5] instead of [5, 10]
            val.sort()
            a, b = val
            helper[b].append((a, idx))

        for idx in range(n + 1):
            helper[idx].sort()

        prevBlockerLocation = [0, None]
        blockerLocation = [0, None]
        cntr = Counter()
        res = []
        for i in range(1, n + 1):
            for newBlockerLocation in helper[i]:
                if blockerLocation[1] is None or newBlockerLocation[0] > blockerLocation[0]:
                    blockerLocation, prevBlockerLocation = newBlockerLocation, blockerLocation
                elif prevBlockerLocation[1] is None or newBlockerLocation[0] > prevBlockerLocation[0]:
                    prevBlockerLocation = newBlockerLocation
            res.append(i - blockerLocation[0])

            if blockerLocation[1] is not None:
                cntr[blockerLocation[1]] += blockerLocation[0] - prevBlockerLocation[0]

        return sum(res) + max(cntr.values())

