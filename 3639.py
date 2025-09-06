"""
Original question: https://leetcode.com/problems/minimum-time-to-activate-string
The bisect_left function's key parameter really saves tons of boilerplate code!
The "True" simply means which is the leftmost point in [0:N] that is True  
"""
from typing import List
from bisect import bisect_left

class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        N = len(s)
        if sum(range(N + 1)) < k:
            return -1
        
        def works(num):
            starLocations = set(order[:num + 1])
            lastSeen = -1
            res = 0
            for idx in range(N):
                if idx not in starLocations:
                    continue
                res += (idx - lastSeen) * (N - idx)
                lastSeen = idx
            return res >= k 

        return bisect_left(range(len(s) + 1), True, key=works)
    