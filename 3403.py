"""
Original question: https://leetcode.com/problems/count-special-subsequences
"""

from typing import List
from collections import Counter

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0
        right = Counter()
        for rIdx in range(3, N):
            for sIdx in range(rIdx + 2, N):
                right[nums[sIdx] / nums[rIdx]] += 1

        for qIdx in range(2, N - 4):
            r = nums[qIdx + 1]
            for sIdx in range(qIdx + 3, N):
                right[nums[sIdx] / r] -= 1
            
            for pIdx in range(qIdx - 2, -1, -1):
                res += right[nums[pIdx] / nums[qIdx]]
        
        return res