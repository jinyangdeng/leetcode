"""
Original question: https://leetcode.com/problems/shortest-matching-substring
An interesting combination of KMP + Binary search
"""

import bisect


def lps(p):
    N = len(p)
    res = [0 for i in range(N)]
    j = 0
    for i in range(1, N):
        while j > 0 and p[i] != p[j]:
            j = res[j - 1]
        if p[i] == p[j]:
            j += 1
        res[i] = j
    return res


def getPattern(s, p):
    N = len(s)
    matches = []
    pat = lps(p)
    j = 0
    for i in range(N):
        while j > 0 and s[i] != p[j]:
            j = pat[j - 1]
        if s[i] == p[j]:
            j += 1
        if j == len(p):
            j = pat[j - 1]
            matches.append(i - len(p) + 1)
    return matches


class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        p = p.split('*')
        p = [e for e in p if e != '']
        if len(p) == 0:
            return 0

        locs = []
        for substr in p:
            locs.append(getPattern(s, substr))

        res = float('inf')

        def dfs(locIdx, sIdx, beginSIdx):
            if locIdx == len(locs):
                return sIdx - beginSIdx

            idx = bisect.bisect_left(locs[locIdx], sIdx)
            if idx != len(locs[locIdx]):
                return dfs(locIdx + 1, locs[locIdx][idx] + len(p[locIdx]), beginSIdx)
            return float('inf')

        for i in range(len(locs[0])):
            res = min(res, dfs(1, locs[0][i] + len(p[0]), locs[0][i]))

        return res if res != float('inf') else -1
