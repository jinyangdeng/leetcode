"""
Original question: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k
ChatGPT generated code. I would have done something similar
"""

from typing import List
from collections import deque

MOD = 10**9 + 7

class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: one way to partition empty prefix
        prefix_sum = [0] * (n + 1)
        prefix_sum[0] = 1  # To calculate range sums efficiently

        # Monotonic deques to maintain max and min in the current window
        min_deque = deque()
        max_deque = deque()
        
        left = 0  # Start of the current window

        for right in range(n):
            # Expand window and update deques
            while min_deque and nums[right] < min_deque[-1]:
                min_deque.pop()
            min_deque.append(nums[right])

            while max_deque and nums[right] > max_deque[-1]:
                max_deque.pop()
            max_deque.append(nums[right])

            # Shrink window from the left if the constraint is violated
            while max_deque[0] - min_deque[0] > k:
                if nums[left] == min_deque[0]:
                    min_deque.popleft()
                if nums[left] == max_deque[0]:
                    max_deque.popleft()
                left += 1

            # dp[right + 1] = sum(dp[left:right+1])
            dp[right + 1] = (prefix_sum[right] - prefix_sum[left - 1] if left > 0 else prefix_sum[right]) % MOD
            prefix_sum[right + 1] = (prefix_sum[right] + dp[right + 1]) % MOD

        return dp[n]
