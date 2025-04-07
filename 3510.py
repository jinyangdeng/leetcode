"""
Original question: https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii
Feels like linked list.

I tried to be smart, and do things like
if nums[first] < nums[before_first] and nums[before_first] <= ssum and (_next[second] is None or not (nums[_next[second]] >= nums[second] and nums[_next[second]] < ssum)):

But complexity begets complexity, and that just makes things harder to debug.
So, I just write:
if nums[first] < nums[before_first] and nums[before_first] <= ssum:
    num_violations -= 1
if nums[first] >= nums[before_first] and nums[before_first] > ssum:
    num_violations += 1
"""

from typing import List
from collections import Counter
import heapq


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)
        num_violations = 0
        _next = [i for i in range(1, N)] + [None]
        _prev = [None] + [i for i in range(N - 1)]
        h = []
        for i in range(N - 1):
            num_violations += nums[i] > nums[i + 1]
            heapq.heappush(h, [nums[i] + nums[i + 1], i])
        
        if num_violations == 0:
            return 0

        res = 0
        deleted_indices = set()
        deleted_pairs = Counter()
        while True:
            if num_violations == 0:
                return res
            ssum, first = heapq.heappop(h)
            if deleted_pairs[(ssum, first)] > 0:
                deleted_pairs[(ssum, first)] -= 1
                continue
            if first in deleted_indices:
                continue
            
            res += 1
            second = _next[first]
            deleted_indices.add(second)
            if _prev[first] is not None:
                before_first = _prev[first]
                oldSum = nums[before_first] + nums[first]
                deleted_pairs[(oldSum, before_first)] += 1
                if nums[first] < nums[before_first] and nums[before_first] <= ssum:
                    num_violations -= 1
                if nums[first] >= nums[before_first] and nums[before_first] > ssum:
                    num_violations += 1
                heapq.heappush(h, [nums[before_first] + ssum, before_first])
            
            
            if _next[second] is not None:
                after_second = _next[second]
                oldSum = nums[second] + nums[after_second]
                deleted_pairs[(oldSum, second)] += 1
                if nums[second] > nums[after_second] and nums[after_second] >= ssum:
                    num_violations -= 1
                if nums[second] <= nums[after_second] and nums[after_second] < ssum:
                    num_violations += 1
                heapq.heappush(h, [nums[after_second] + ssum, first])
            
            _next[first] = _next[second]
            if _next[second] is not None:
                _prev[_next[second]] = first   
            
            if nums[second] < nums[first]:
                num_violations -= 1

            nums[first] = ssum
            nums[second] = None
