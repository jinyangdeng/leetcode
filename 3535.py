"""
Original question: https://leetcode.com/problems/unit-conversion-ii
The challenge is in finding the multiplicative inverse of q mod 1_000_000_007
i.e. given 2, 2 * WHAT mod 1_000_000_007 = 1?

According to Fermat's little theorem, when m is prime.
a^(m - 1) mod m = 1
so a * a^(m - 2) mod m = 1

so the WHAT = a ^(m - 2)
"""

from typing import List
from collections import deque

class Solution:
    def queryConversions(self, conversions: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 1_000_000_007

        helper = [[] for i in range((len(conversions) + 1))]
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
        
        return [pow(mapping[a], MOD - 2, MOD) * mapping[b] % MOD for a, b in queries]
    