"""
Original question: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i
"""

from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        counter = Counter(s)
        maxOdd = max(val for val in counter.values() if val % 2 == 1)
        minEven = min(val for val in counter.values() if val % 2 == 0)
        return maxOdd - minEven
