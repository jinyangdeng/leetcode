"""
Original question: https://leetcode.com/problems/sum-of-perfect-square-ancestors
"""
from collections import defaultdict, Counter
from typing import List

class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            for possible_sqrt in range(int(num ** 0.5), 1, -1):
                if num % (possible_sqrt ** 2) == 0:
                    num = num // (possible_sqrt ** 2)
            nums[i] = num

        adjList = defaultdict(list)

        for _f, _t in edges:
            adjList[_f].append(_t)
            adjList[_t].append(_f)
        
        cntr = Counter()

        def dfs(curr, prev):
            current_sum = cntr[nums[curr]]
            cntr[nums[curr]] += 1
            for nghb in adjList[curr]:
                if nghb == prev:
                    continue
                current_sum += dfs(nghb, curr)
            cntr[nums[curr]] -= 1
            return current_sum
        
        return dfs(0, -1)