"""
Original question: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii

Kudos to: https://www.youtube.com/watch?v=9J3hrtjHBAg for explanation
Interesting to transform the problem into kadane problem with sliding window. Originally, I implemented a deque buffer,
ensuring that it is at least size k and contains >= 2 even chars and >= 1 odd char However, having such a deque will
result in O(k) memory. Hence, by just tracking the left and right of the sliding window, I keep it to O(1) memory.
"""

from math import inf


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        chars = ['0', '1', '2', '3', '4']

        res = -inf
        for oddChar in chars:
            for evenChar in chars:
                if oddChar == evenChar:
                    continue

                oddCharCount, evenCharCount = 0, 0
                helper = {(oddCharCount % 2, evenCharCount % 2): 0}

                left = 0
                leftOddCharCount, leftEvenCharCount = 0, 0
                for right, char in enumerate(s):
                    oddCharCount += char == oddChar
                    evenCharCount += char == evenChar

                    while ((right - left >= k)
                           and not (s[left] == oddChar and oddCharCount - leftOddCharCount <= 1)
                           and not (s[left] == evenChar and evenCharCount - leftEvenCharCount <= 2)):
                        leftOddCharCount += s[left] == oddChar
                        leftEvenCharCount += s[left] == evenChar
                        helper[(leftOddCharCount % 2, leftEvenCharCount % 2)] = min(
                            leftOddCharCount - leftEvenCharCount,
                            helper.get((leftOddCharCount % 2, leftEvenCharCount % 2), inf))
                        left += 1

                    if (right - left >= k - 1) and (oddCharCount - leftOddCharCount >= 1) and (
                            evenCharCount - leftEvenCharCount >= 2):
                        oppositeKey = (1 - oddCharCount % 2, evenCharCount % 2)
                        if oppositeKey in helper:
                            res = max(res, oddCharCount - evenCharCount - helper[oppositeKey])

        return res
