"""
Original question: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions
"""

from typing import List


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        m = len(mana)

        nnext = 0
        for i in range(m - 1):
            curr = nnext
            cumSkill = 0
            for s in skill:
                curr += s * mana[i]
                nnext = max(nnext, curr - cumSkill * mana[i + 1])
                cumSkill += s

        return nnext + sum(skill) * mana[-1]
