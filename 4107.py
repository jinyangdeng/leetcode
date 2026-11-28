"""
Original question: https://leetcode.com/problems/count-valid-suffix-sorts-i
感想: 真的要去读懂题目啊
一开始以为 “resulting (sub)array is equal to (the same position in) target.”，但需要整体一样
"""

class Solution:
    def countSuffix(self, nums: list[int], target: list[int]) -> int:
        n = len(nums)
        tracker = dict()

        equal = True
        frontEquals = [True]
        for n1, n2 in zip(nums[:-1], target[:-1]):
            equal = equal and (n1 == n2)
            frontEquals.append(equal)

        res = 0
        for i in range(n-1, -1, -1):
            if i != n-1 and target[i] < target[i+1]:
                break
            t, num = target[i], nums[i]
            tracker[t] = tracker.get(t, 0) + 1
            tracker[num] = tracker.get(num, 0) - 1

            if tracker[t] == 0:
                del tracker[t]
            if num != t and tracker[num] == 0:
                del tracker[num] 

            res += (len(tracker) == 0 and frontEquals[i])

        return res