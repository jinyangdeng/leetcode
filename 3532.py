"""
Original question: https://leetcode.com/problems/path-existence-queries-in-a-graph-i
"""

from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if rank[px] <= rank[py]:
                parent[px] = py
                rank[py] += 1
            else:
                parent[py] = px
                rank[px] += 1        
        

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] <= maxDiff:
                union(i, i - 1)
        
        return [find(u) == find(y) for u, y in queries]
        