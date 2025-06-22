"""
Original question: https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence
ChatGPT couldn't solve this.
"""

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        return max(self._max_product(nums, m), self._max_product(nums[::-1], m))

    def _max_product(self, nums: List[int], m: int) -> int:
        window_size = m - 1
        min_val = float('inf')
        max_val = float('-inf')
        max_product = float('-inf')

        for i in range(len(nums)):
            if i >= window_size:
                candidate = nums[i - window_size]
                min_val = min(min_val, candidate)
                max_val = max(max_val, candidate)
                max_product = max(
                    max_product,
                    min_val * nums[i],
                    max_val * nums[i]
                )

        return max_product
