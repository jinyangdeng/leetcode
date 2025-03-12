"""
Original question: https://leetcode.com/problems/choose-k-elements-with-maximum-sum
"""
from collections import defaultdict
from typing import List
import heapq


class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        helper = defaultdict(list)
        for idx, num1 in enumerate(nums1):
            helper[num1].append((nums2[idx], idx))

        sorted_helper = sorted(helper.items())

        h = []
        ssum = 0
        res = [0] * len(nums1)

        for _, items in sorted_helper:
            for num2, idx in items:
                res[idx] = ssum

            for num2, _ in items:
                heapq.heappush(h, num2)
                ssum += num2

            while len(h) > k:
                ssum -= heapq.heappop(h)

        return res
