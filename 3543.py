"""
Original question: https://leetcode.com/problems/maximum-weighted-k-edge-path
"""
from typing import List
from collections import deque

class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        parents = [[] for _ in range(n)]
        outs = [0 for _ in range(n)]

        for f, _t, w in edges:
            parents[_t].append((f, w))
            outs[f] += 1
        
        dp = [[set() for _ in range(k + 1)] for _ in range(n)]
        for i in range(n):
            dp[i][0] = set([0])

        q = deque([])
        for i in range(n):
            if outs[i] == 0:
                q.append(i)
        
        res = -1
        while q:
            num = q.popleft()

            for cand in dp[num][k]:
                res = max(res, cand)
            
            for parent, weight in parents[num]:
                outs[parent] -= 1
                if outs[parent] == 0:
                    q.append(parent)
                for step in range(k):
                    for weightSum in dp[num][step]:
                        if weightSum + weight < t:
                            dp[parent][step + 1].add(weightSum + weight)
                
        return res
