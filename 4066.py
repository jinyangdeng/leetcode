"""
Original question: https://leetcode.com/problems/maximum-equal-adjacent-pairs-after-at-most-one-replacement
好久没做了，感觉脑袋都生锈了
1. pairwise 就不用去写 for i in range(len(nums) - 1) 了
2. max([...], default = 0) 里的这个 default = 0 很重要，防止 pairs.values() 是空的
"""
from collections import Counter
from itertools import pairwise

class Solution:
    def maxEqualAdjacentPairs(self, nums: list[int]) -> int:
        # cntr = defaultdict(int)

        # alreadySame = 0

        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         alreadySame += 1
        #         continue

        #     key = (min(nums[i], nums[i + 1]), max(nums[i], nums[i + 1]))
        #     cntr[key] += 1

        # if len(cntr.values()) == 0:
        #     return alreadySame
        # return max(cntr.values()) + alreadySame

        
        same = 0
        pairs = Counter()
        for a, b in pairwise(nums):
            if a == b:
                same += 1
            else:
                pairs[min(a, b), max(a, b)] += 1
        return max(pairs.values(), default = 0) + same