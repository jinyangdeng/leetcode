"""
Original question: https://leetcode.com/problems/find-mismatched-segments-between-two-strings
非常容易，不应该是 Medium
"""


class Solution:
    def findMismatchedSegments(self, s1: str, s2: str) -> list[list[str]]:
        diffs = []
        helper = []

        n = len(s1)
        for i in range(n):
            if s1[i] == s2[i]:
                if len(helper) != 0:
                    diffs.append([''.join(s1[j] for j in helper), ''.join(s2[j] for j in helper)])
                helper = []
            else:
                helper.append(i)
        
        if len(helper) != 0:
            diffs.append([''.join(s1[j] for j in helper), ''.join(s2[j] for j in helper)])
        
        return diffs