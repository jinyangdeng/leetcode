"""
Original question: https://leetcode.com/problems/jump-game-ix
"""
from typing import List

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # 很容易掉进一个误区，那就是:
        # 仅靠左边有没有比自己大的数字，右边有没有比自己小的数字来决定要不要继续，还是切断。
        # 这并不靠谱，因为:
        # - 如果左边有比自己大的数字，肯定不会切断 (either before or after me)
        # - 那难道就只看右边有没有比自己小的数字了吗？
        # -- 如果没有比自己小的数字，就切断？这行不通。E.g. 3, 1, 2，在1的时候不能切断
        # -- 如果有比自己小的数字，就切断？这也行不通。E.g. 3, 2, 1，在3的时候不能切断
        # 需要一种 “大局观”
        rightMin = [0] * len(nums)
        mmin = float('inf')
        for idx in range(len(nums) - 1, -1, -1):
            rightMin[idx] = mmin
            mmin = min(mmin, nums[idx])

        start = 0
        leftMaxUntilMe = 0
        res = [0] * len(nums)
        for idx, val in enumerate(nums):
            leftMaxUntilMe = max(leftMaxUntilMe, val)
            if leftMaxUntilMe <= rightMin[idx]:
                res[start:idx + 1] = [leftMaxUntilMe] * (idx + 1 - start)
                start = idx + 1     

        return res
    