"""
Original question: https://leetcode.com/problems/maximize-active-section-with-trade-ii
"""
import bisect
import math
from typing import List


class SegmentTree:
    def __init__(self, values: List[List[int]]):
        self.N = 2 ** math.ceil(math.log2(len(values)))
        self.values = [0] * 2 * self.N
        for idx, val in enumerate(values):
            self.update(self.N + idx, val[1] - val[0] + val[3] - val[2])

    def update(self, idx, val):
        self.values[idx] = val
        while idx > 1:
            self.values[idx // 2] = max(self.values[idx], self.values[idx ^ 1])
            idx = idx // 2

    def query(self, leftIdx, rightIdx):
        leftIdx += self.N
        rightIdx += self.N
        max_val = float('-inf')
        while leftIdx < rightIdx:
            # print("query: ", leftIdx, ": ", rightIdx)
            if leftIdx & 1:
                max_val = max(max_val, self.values[leftIdx])
                leftIdx += 1
            if rightIdx & 1:
                rightIdx -= 1
                max_val = max(max_val, self.values[rightIdx])

            leftIdx //= 2
            rightIdx //= 2
        return max_val


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        helper = []
        for idx, val in enumerate(s):
            if len(helper) == 0 or helper[-1][0] != int(val):
                helper.append([int(val), idx, idx])
            else:
                helper[-1][2] = idx

        compressed = []
        for i in range(1, len(helper) - 1):
            if helper[i][0] == 1:
                compressed.append([helper[i - 1][1], helper[i][1], helper[i][2], helper[i + 1][2]])

        original_count = s.count('1')
        if len(compressed) == 0:
            return [original_count] * len(queries)

        st = SegmentTree(compressed)

        res = []
        for left, right in queries:
            currRes = original_count
            leftIdx = bisect.bisect_left(compressed, left, key=lambda x:x[0], hi=len(compressed) - 1)
            rightIdx = bisect.bisect_left(compressed, right, key=lambda x:x[-1], hi=len(compressed) - 1)
            if leftIdx > 0 and compressed[leftIdx][0] > left:
                leftIdx -= 1

            for idx in [leftIdx, rightIdx]:
                zeroLeft, oneLeft, oneRight, zeroRight = compressed[idx]
                if left < oneLeft and oneRight < right:
                    currRes = max(currRes, original_count + oneLeft - max(left, zeroLeft) + min(right, zeroRight) - oneRight)

            if leftIdx + 1 < rightIdx:
                currRes = max(currRes, original_count + st.query(leftIdx + 1, rightIdx))
            res.append(currRes)

        return res
