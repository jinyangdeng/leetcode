"""
Original question: https://leetcode.com/problems/count-special-triplets
ChatGPT generated code. Same as what I would have written.
"""

from collections import defaultdict
from typing import List

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        result = 0

        suffix = defaultdict(int)
        for num in nums:
            suffix[num] += 1

        prefix = defaultdict(int)

        for j in range(n):
            suffix[nums[j]] -= 1  # nums[j] is now being processed

            target = nums[j] * 2
            left = prefix[target]
            right = suffix[target]

            result = (result + left * right) % MOD

            prefix[nums[j]] += 1  # Update prefix for future j

        return result