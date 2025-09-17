"""
Original question: https://leetcode.com/problems/subsequence-sum-after-capping-elements
lru_cache(maxsize=None) will cause memory size exceeded :(
"""
from typing import List
from collections import deque

class Solution:
    def subsequenceSumAfterCapping(self, nums: List[int], k: int) -> List[bool]:
        nums.sort()
        memo = [[None for i in range(k + 1)] for i in range(len(nums))]

        def dp(idx, remaining):
            if memo[idx][remaining] is not None:
                return memo[idx][remaining]

            if remaining == 0:
                return True

            if idx == -1:
                return False
            
            if usableNumbers[idx] > remaining:
                memo[idx][remaining] = dp(idx - 1, remaining)
                return memo[idx][remaining]
            memo[idx][remaining] = dp(idx - 1, remaining) or dp(idx - 1, remaining - usableNumbers[idx])
            return memo[idx][remaining]
        
        res = []
        nums = deque(nums)
        usableNumbers = []

        for i in range(1, len(nums) + 1):
            while nums and nums[0] <= i:
                usableNumbers.append(nums.popleft())

            maxDeductible = len(nums) * i
            for deduct in range(0, min(k, maxDeductible) + 1, i):
                if dp(len(usableNumbers) - 1, k - deduct):
                    res.append(True)
                    break
            else:
                res.append(False)
        
        return res