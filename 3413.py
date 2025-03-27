"""
Original question: https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags
Bisect is just so untidy here
"""
import bisect
from typing import List


class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()

        helper = []
        cumSum = 0
        for start, stop, coin in coins:
            helper.append([start, stop, cumSum, coin])
            cumSum += (stop - start + 1) * coin

        res = 0
        for start, stop, cumSum, coin in helper:
            end = start + k - 1
            idx = bisect.bisect_left(helper, [end, 0, 0, 0], hi=len(helper) - 1)
            if helper[idx][0] > end and idx > 0:
                idx -= 1
            res = max(res, helper[idx][2] - cumSum + (min(end, helper[idx][1]) - helper[idx][0] + 1) * helper[idx][3])

            begin = stop - k + 1
            idx = bisect.bisect_left(helper, [begin, 0, 0, 0], hi=len(helper) - 1)
            if helper[idx][0] > begin and idx > 0:
                idx -= 1
            res = max(res, cumSum + (stop - start + 1) * coin - helper[idx][2] - (max(min(begin, helper[idx][1] + 1) - helper[idx][0], 0) * helper[idx][3]))
        return res
