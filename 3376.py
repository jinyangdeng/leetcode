"""
Original question: https://leetcode.com/problems/minimum-time-to-break-locks-i/
My initial approach is to sort the lock, then look at the weakest lock, how long it takes to accumulate
sufficient energy, do that, but break the strongest lock possible.

But it fails at the following scenario:
current energy 17, strength: [18, 50], k = 1
My initial approach: wait for 2 days, break 18, my k becomes 18, wait for another 3 days, break 50
Correct approach: wait for 3 days, break 50, my k becomes 18, wait for 1 day, break 18
"""

from functools import lru_cache
from typing import List
import math

class Solution:
    def findMinimumTime(self, strength: List[int], k: int) -> int:
        N = len(strength)

        # curr ranges between 1, 1 + k, 1 + len(strength)) * k
        # flag has 1 << len(strength)
        @lru_cache(maxsize=None)
        def recurse(flag, curr):
            if flag == 0:
                return 0

            res = float('inf')
            for i in range(N):
                if flag & (1 << i) != 0:
                    res = min(res, math.ceil(strength[i] / curr) + recurse(flag ^ (1 << i), curr + k))

            return res

        return recurse((1 << N) - 1, 1)