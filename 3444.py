"""
Original question: https://leetcode.com/problems/minimum-increments-for-target-multiples-in-an-array
这道题比较难的一点是: 你会想去建立一个 set of used nums
这样也行，可是就感觉没这么优美了

一个坑是 nums: [1, 98] target: [7, 100]
要是你一个一个看 target，7最适合98，可这样一来，100和1搭配，会导致很多 increment
方法：一个一个看 num，重复计算着，要是我选这几个数字 (bitmask)，会导致这几个 state 有什么变化？
"""
import sys
from typing import List
from math import lcm

class Solution:
    def minimumIncrements(self, nums: List[int], target: List[int]) -> int:
        targetN = len(target)
        lcms = [0] * (1 << targetN)
        for bitmask in range(1, 1 << targetN):
            lcn = 1
            for idx in range(targetN):
                if bitmask & (1 << idx):
                    lcn = lcm(lcn, target[idx])
            lcms[bitmask] = lcn

        dp = [sys.maxsize] * (1 << targetN)
        dp[0] = 0

        for num in nums:
            new = dp[:]

            for bitmask in range(1, 1 << targetN):
                _lcm = lcms[bitmask]
                # how much must I increment num, before it is divisible by _lcm
                cost = (_lcm - num % _lcm) % _lcm

                for existingBitmask in range(1 << targetN):
                    new[existingBitmask | bitmask] = min(new[existingBitmask | bitmask], dp[existingBitmask] + cost)

            dp = new

        return dp[-1]