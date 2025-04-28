"""
Original question: https://leetcode.com/problems/concatenated-divisibility
"""

from typing import List
from functools import lru_cache

class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        N = len(nums)
        @lru_cache(maxsize = None)
        def dp(idx, used, rem):
            if idx == N:
                return rem == 0
            for i in range(N):
                if (used >> i) & 1 == 1:
                    continue
                if dp(idx + 1, used | (1 << i), (rem * 10**(len(str(nums[i]))) + nums[i]) % k):
                    return True
            return False 
        
        if dp(0, 0, 0) == False:
            return []
        
        used = 0
        rem = 0
        res = []
        for idx in range(N):
            for i in range(N):
                if (used >> i) & 1 == 1:
                    continue

                if dp(idx + 1, used | (1 << i), (rem * 10**(len(str(nums[i]))) + nums[i]) % k) == True:
                    res.append(nums[i])
                    used = used | (1 << i)
                    rem = (rem * 10**(len(str(nums[i]))) + nums[i]) % k
                    break 

        return res
    