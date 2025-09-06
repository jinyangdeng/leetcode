"""
Original question: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy
itertools.accumulate 很好用
"""
from typing import List
from itertools import accumulate

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        effects = [p * s for p, s in zip(prices, strategy)]

        cumSumEffects = list(accumulate(effects, initial=0))
        
        cumSumPrices = list(accumulate(prices, initial=0))

        originalProfit = cumSumEffects[-1]

        maxProfitWithModification = float('-inf')
        for i in range(k // 2, len(prices) - k // 2 + 1):
            maxProfitWithModification = max(maxProfitWithModification, originalProfit - (cumSumEffects[i + k//2] - cumSumEffects[i - k//2]) + (cumSumPrices[i + k//2] - cumSumPrices[i]))

        return max(maxProfitWithModification, originalProfit)
