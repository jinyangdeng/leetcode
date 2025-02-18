"""
Original question: https://leetcode.com/problems/select-k-disjoint-special-substrings
The hardest part is constructing the non-overlapping intervals.
E.g. abbacbece
Even though char 'a' appeared at indices 0 and 3, to have a string with both 'a's, will include 'b's, then 'c's,
then 'e's
"""
from functools import lru_cache


class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        N = len(s)
        charset = set(s)
        first, last = dict(), dict()
        for idx, char in enumerate(s):
            first[char] = first.get(char, idx)
            last[char] = idx

        helper = [[char, first[char], last[char]] for char in charset]
        helper.sort(key=lambda x: x[1])
        for char, _from, _to in helper:
            first[char] = min(first[middleChar] for middleChar in set(s[_from:_to + 1]))

        helper.sort(key=lambda x: x[2])
        for char, _from, _to in helper[::-1]:
            last[char] = max(last[middleChar] for middleChar in set(s[_from:_to + 1]))

        @lru_cache(maxsize = None)
        def dp(idx, k):
            if k == 0:
                return True

            # At this point in time, the charset doesn't even matter.
            # We only care about which of the non-overlapping intervals can we take up from this point.
            for char in charset:
                if first[char] >= idx and last[char] - first[char] + 1 != N:
                    if dp(last[char] + 1, k - 1):
                        return True
            return False

        return dp(0, k)