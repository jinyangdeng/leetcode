"""
Original question: https://leetcode.com/problems/properties-graph
"""
from typing import List


def intersect(arr1, arr2):
    return len(arr1.intersection(arr2))


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        N = len(properties)
        for i in range(N):
            properties[i] = set(properties[i])

        parents = [i for i in range(N)]
        ranks = [1] * N

        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if ranks[px] >= ranks[py]:
                parents[py] = px
                ranks[px] += 1
            else:
                parents[px] = py
                ranks[py] += 1

        for i in range(N):
            for j in range(i + 1, N):
                if intersect(properties[i], properties[j]) >= k:
                    union(i, j)

        for i in range(N):
            find(i)

        return len(set(parents))
