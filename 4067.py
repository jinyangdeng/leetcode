"""
Original question: https://leetcode.com/problems/longest-subarray-with-restricted-pair-sums
1. 很容易遗漏 banned[num - prev] = max(banned[num - prev], window[prev]). 要去想 prev 和 num 能玩出什么花样来
2. 这个是优化:
    if window[nums[left]] == left:
        del window[nums[left]]
"""

from collections import defaultdict
from typing import List

class Solution:
    def maxSubarray(self, nums: List[int]) -> int:
        res = 0

        left = 0
        window = dict()
        banned = defaultdict(int)
        for right, num in enumerate(nums):
            if num in banned:
                while left <= banned[num]:
                    if window[nums[left]] == left:
                        del window[nums[left]]
                    left += 1
            
            for prev in window:
                # prev = nums[i], num = nums[j], I want to ban nums[k]
                banned[prev + num] = max(banned[prev + num], window[prev])
                # prev = nums[k], num = nums[i], I want to ban nums[j]
                banned[prev - num] = max(banned[prev - num], window[prev])
                # num = nums[k], prev = nums[i], I want to ban nums[j]
                banned[num - prev] = max(banned[num - prev], window[prev])

            window[num] = right
            res = max(res, right - left + 1)
            
        return res