"""
Original question: https://leetcode.com/problems/number-of-intersecting-interval-pairs-ii
脑袋太锈了，"or end <= heap[0]" 竟然遗漏了
"""

import heapq


class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        res = 0
        heap = []
        intervals.sort()

        for start, end in intervals:
            while heap and not (start <= heap[0] <= end or end <= heap[0]):
                heapq.heappop(heap)
            res += len(heap)
            heapq.heappush(heap, end)
        
        return res
