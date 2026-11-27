"""
Original question: https://leetcode.com/problems/minimum-cost-to-make-all-array-elements-equal
很容易遗漏 "0 < i < n - 1" 的条件
"""


class Solution:
    def minCost(self, nums: list[int]) -> int:
        N = len(nums)
        res = float('inf')
        leftIdx = 1
        while leftIdx < N - 1:
            rightIdx = leftIdx
            while rightIdx + 1 < N-1 and nums[rightIdx] == nums[rightIdx + 1]:
                rightIdx += 1
            if leftIdx == 1 and nums[0] == nums[1]:
                leftCost = 0
            else:
                leftCost = leftIdx * nums[leftIdx]

            if rightIdx == N - 2 and nums[N-2] == nums[N-1]:
                rightCost = 0
            else:
                rightCost = (N - 1 - rightIdx) * nums[leftIdx]
            
            res = min(res, leftCost + rightCost)
            leftIdx = rightIdx + 1
        return res