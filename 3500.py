"""
Original question: https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays
The trick is figuring how the i in k * i can be simplified away  
"""
from typing import List
from itertools import accumulate


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        numPrefixSum = list(accumulate(nums, initial = 0))
        costPrefixSum = list(accumulate(cost, initial = 0))

        N = len(nums)
        dp = [float('inf')] * (N + 1)
        dp[-1] = 0

        for i in range(N - 1, -1, -1):
            for j in range(N, i, - 1):
                dp[i] = min(dp[i], dp[j] + k * (costPrefixSum[-1] - costPrefixSum[i]) + (numPrefixSum[j] - numPrefixSum[i]) * (costPrefixSum[-1] - costPrefixSum[i]))
            
        return dp[0]
