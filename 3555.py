"""
Original question: https://leetcode.com/problems/smallest-subarray-to-sort-in-every-sliding-window
"""

from typing import List

class Solution:
    def minSubarraySort(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n - k + 1):
            originalrange = nums[i:i + k]
            sortedrange = sorted(originalrange)

            left, right = 0, k - 1

            while left < k and originalrange[left] == sortedrange[left]:
                left += 1

            while right > left and originalrange[right] == sortedrange[right]:
                right -= 1

            res.append(0 if left > right else right - left + 1)

        return res