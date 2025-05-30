"""
Original question: https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i
The dfs is template.
The hard part is realizing you only need to pin down 1 edge and let loose all the other edges.
For each of the other edges, they can either be a 1 or 2, i.e. 2 choices.
What matters, is the other edges will always add up to either an odd or even sum.
And that means you have no choice for the 1 edge that is pinned down:
- If the sum is odd, you assign 2 to the pinned edge to keep the total sum odd.
- If the sum is even, you assign 1 to the pinned edge to keep the total sum odd.
"""

from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        def max_depth(edges):
            from collections import defaultdict, deque

            n = len(edges) + 1
            tree = defaultdict(list)
            for u, v in edges:
                tree[u].append(v)
                tree[v].append(u)

            visited = [False] * (n + 1)
            stack = [(1, 0)]  # (node, depth)
            max_depth = 0

            while stack:
                node, depth = stack.pop()
                if visited[node]:
                    continue
                visited[node] = True
                max_depth = max(max_depth, depth)
                for neighbor in tree[node]:
                    if not visited[neighbor]:
                        stack.append((neighbor, depth + 1))

            return max_depth
        
        return pow(2, max_depth(edges) - 1, 1_000_000_007)
