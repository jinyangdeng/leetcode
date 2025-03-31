"""
Original question: https://leetcode.com/problems/maximize-active-section-with-trade-i
"""

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        compress = []
        for char in s:
            if len(compress) > 0 and char == compress[-1][0]:
                compress[-1][1] += 1
            else:
                compress.append([char, 1])
        
        total1 = s.count('1')
        res = total1
        for i in range(1, len(compress) - 1):
            if compress[i][0] == '1':
                res = max(res, total1 + compress[i - 1][1] + compress[i + 1][1])
                
        return res
    