"""
Original quesiton: https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals

#TODO: Need to clean up. Really untidy
"""

from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        N = len(intervals)

        helper = []
        for idx, interval in enumerate(intervals):
            l, r, weight = interval
            helper.append([r, idx, weight])
        helper.sort()

        dp = [[[0, []] for idx in range(N)] for i in range(4)]
        dp[0] = [[intervals[helper[idx][1]][2], [helper[idx][1]]] for idx in range(N)]
        
        for idx in range(1, N):
            intervalIdx = helper[idx][1]
            l, r, w = intervals[intervalIdx]

            for k in range(0, 4):
                if dp[k][idx - 1][0] > dp[k][idx][0] or (dp[k][idx - 1][0] == dp[k][idx][0] and dp[k][idx - 1][1] < dp[k][idx][1]):
                    dp[k][idx] = [dp[k][idx - 1][0], dp[k][idx - 1][1][:]]                     
                if k > 0:
                    prevIdx = bisect.bisect_left(helper, [l - 1, float('inf')])
                    if helper[prevIdx][0] > l - 1:
                        prevIdx -= 1
                    if prevIdx < 0:
                        continue
                    if dp[k - 1][prevIdx][0] + w > dp[k][idx][0] or (dp[k - 1][prevIdx][0] + w == dp[k][idx][0] and sorted(dp[k - 1][prevIdx][1][:] + [intervalIdx]) < dp[k][idx][1]):
                        dp[k][idx] = [dp[k - 1][prevIdx][0] + w, sorted(dp[k - 1][prevIdx][1][:] + [intervalIdx])]
        
        res = []
        score = 0
        for i in range(4):
            if dp[i][-1][0] > score:
                score = dp[i][-1][0]
                res = dp[i][-1][1]
            elif dp[i][-1][0] == score and dp[i][-1][1] < res:
                res = dp[i][-1][1]

        return res