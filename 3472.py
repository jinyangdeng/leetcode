"""
Original question: https://leetcode.com/problems/longest-palindromic-subsequence-after-at-most-k-operations
Using lru_cache will lead to memory limit exceeded.
However, explicitly allocating memory will not.

Trick: When explicitly allocating memory (i.e. constructing list of lists of lists), construct them in the opposite order
of the order of arguments in the dp function.
Eg. dp(leftIdx, rightIdx, kLeft)
so helper innermost dimension is kLeft, then rightIdx, then leftIdx
"""


class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:
        helper = [[[None]*(k+1) for _ in range(len(s))] for _ in range(len(s))]

        # @lru_cache(maxsize = None)
        def dp(leftIdx, rightIdx, kLeft):
            if helper[leftIdx][rightIdx][kLeft] != None:
                return helper[leftIdx][rightIdx][kLeft]
                
            if leftIdx > rightIdx:
                helper[leftIdx][rightIdx][kLeft] = 0
                return 0
            if leftIdx == rightIdx:
                helper[leftIdx][rightIdx][kLeft] = 1
                return 1
            
            diff = min(
                max(ord(s[leftIdx]), ord(s[rightIdx])) - min(ord(s[leftIdx]), ord(s[rightIdx])),
                min(ord(s[leftIdx]), ord(s[rightIdx])) - ord('a') + 1 + ord('z') - max(ord(s[leftIdx]), ord(s[rightIdx]))
            )
            
            if diff > kLeft:
                helper[leftIdx][rightIdx][kLeft] = max(
                    dp(leftIdx + 1, rightIdx, kLeft),
                    dp(leftIdx, rightIdx - 1, kLeft)
                )
            else:
                helper[leftIdx][rightIdx][kLeft] = max(
                    dp(leftIdx + 1, rightIdx, kLeft),
                    dp(leftIdx, rightIdx - 1, kLeft),
                    2 + dp(leftIdx + 1, rightIdx - 1, kLeft - diff)
                )           

            return helper[leftIdx][rightIdx][kLeft]

        return dp(0, len(s) - 1, k)