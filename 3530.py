"""
Original question: https://leetcode.com/problems/maximum-profit-from-valid-topological-order-in-dag
Needed that optimisation trick when edges is an empty list 
"""

from typing import List
from collections import defaultdict

class Solution:
    def maxProfit(self, n: int, edges: List[List[int]], score: List[int]) -> int:
        if len(edges) == 0:
            return sum((i + 1) * score for i, score in enumerate(sorted(score)))
        
        requirements = defaultdict(int)
        for u, v in edges:
            requirements[v] |= 1 << u
        
        prev = {0: 0}

        for step in range(n):
            new = {}
            for current in prev:
                for candidate in range(n):
                    if (current >> candidate) & 1 == 1:
                        continue
                    if (current & requirements[candidate]) != requirements[candidate]:
                        continue
                    nextState = current | (1 << candidate)
                    if nextState not in new:
                        new[nextState] = prev[current] + (step + 1) * score[candidate]
                    else:
                        new[nextState] = max(new[nextState], prev[current] + (step + 1) * score[candidate])

            prev = new      

        return prev[(1 << n) - 1]
    