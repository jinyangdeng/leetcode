"""
Original question: https://leetcode.com/problems/find-minimum-cost-to-remove-array-elements
Extremely stingy with memory and run time.
top-down with lru_cache -> memory limit exceeded
buttom-up with "sliding window" -> must 1/2 * N^2 to pass time limit
"""

from typing import List

class Solution:
    def minCost(self, nums: List[int]) -> int:
        N = len(nums)
    
        if N < 3:
            return max(nums)
        
        two = nums[:]
        one = nums[:]

        for currIdx in range(N - 1, 2, -1):
            zero = [float('inf')] * N
            
            for carryFromPrevIdx in range(currIdx):
                if N - currIdx + 1 < 3:
                    zero[carryFromPrevIdx] = max(nums[carryFromPrevIdx], max(nums[currIdx:]))
                else:
                    zero[carryFromPrevIdx] = min(
                        max(nums[carryFromPrevIdx], nums[currIdx]) + two[currIdx + 1],
                        max(nums[carryFromPrevIdx], nums[currIdx + 1]) + two[currIdx],
                        max(nums[currIdx], nums[currIdx + 1]) + two[carryFromPrevIdx]
                    )

            one, two = zero, one
        
        return min(
            max(nums[0], nums[1]) + one[2],
            max(nums[0], nums[2]) + one[1],
            max(nums[1], nums[2]) + one[0]
        )