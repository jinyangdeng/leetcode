"""
Original question: https://leetcode.com/problems/count-beautiful-numbers
The allowLeadingZero is a gotcha for me
"""
from functools import cache


class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:
        @cache
        def dp(num, idx, isEdge, allowLeadingZero, product, ssum):
            if idx == len(num):
                return ssum != 0 and product % ssum == 0

            res = 0
            top = int(num[idx]) if isEdge else 9
            for cand in range(top + 1):
                newProduct = 1 if allowLeadingZero and cand == 0 else product * cand
                res += dp(num, idx + 1, isEdge and cand == top, allowLeadingZero and cand == 0, newProduct, ssum + cand)
            return res

        return dp(str(r), 0, True, True, 1, 0) - dp(str(l - 1), 0, True, True, 1, 0)