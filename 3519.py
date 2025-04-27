"""
Original question: https://leetcode.com/problems/count-numbers-with-non-decreasing-digits
"""

from functools import lru_cache


class Solution:
    def convertToBase(self, num: str, newBase: int) -> str:
        num = int(num)
        res = ""
        while num > 0:
            res = str(num % newBase) + res
            num //= newBase
        return res

    def countNumbers(self, l: str, r: str, b: int) -> int:
        MOD = 1_000_000_007

        @lru_cache(None)
        def dp(
            num: str, idx: int, prev_digit: int, is_tight: bool, is_leading_zero: bool
        ):
            if idx == len(num):
                return 1

            upper_bound = int(num[idx]) if is_tight else b - 1

            res = 0
            for digit in range(upper_bound + 1):
                if is_leading_zero or digit >= prev_digit:
                    res += dp(
                        num,
                        idx + 1,
                        digit,
                        is_tight and (digit == upper_bound),
                        is_leading_zero and digit == 0,
                    )
            return res % MOD

        return (
            dp(self.convertToBase(r, b), 0, 0, True, True)
            - dp(self.convertToBase(str(int(l) - 1), b), 0, 0, True, True)
        ) % MOD
