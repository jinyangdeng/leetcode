"""
Original question: https://leetcode.com/problems/unit-conversion-i
"""

from typing import List
from collections import deque

class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 1_000_000_007

        helper = defaultdict(list)
        for src, tgt, cf in conversions:
            helper[src].append([tgt, cf])

        mapping = [0] * (len(conversions) + 1)
        mapping[0] = 1
        q = deque([0])
        while q:
            node = q.popleft()
            for tgt, cf in helper[node]:
                mapping[tgt] = mapping[node] * cf % MOD
                q.append(tgt)
        
        return mapping