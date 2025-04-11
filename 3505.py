"""
Original question: https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal
"""

from sortedcontainers import SortedList
from typing import List

class Solution:
    def get_median(self, nums: List[int], window_size: int):
        medians = []
        window = SortedList([])
        for i in range(len(nums)):
            window.add(nums[i])
            if i < window_size - 1:              
                continue
            if window_size // 2:
                medians.append(window[window_size // 2])
            else:
                medians.append((window[window_size // 2] + window[window_size // 2 + 1]) // 2)
            window.remove(nums[i - window_size + 1])
        return medians

    def get_ops(self, nums: List[int], window_size: int, targets: List[int]):
        lower_sum = 0
        lower_list = SortedList([])
        higher_sum = 0
        higher_list = SortedList([])

        ops = []
        for i in range(window_size - 1):
            lower_list.add(nums[i])
            lower_sum += nums[i]
        
        for i in range(window_size - 1, len(nums)):
            lower_list.add(nums[i])
            lower_sum += nums[i]

            target = targets[i - window_size + 1]
            lower_target_len = window_size // 2 + window_size % 1
            higher_target_len = window_size // 2
            while len(lower_list) > lower_target_len:
                num = lower_list.pop(-1)
                lower_sum -= num
                higher_list.add(num)
                higher_sum += num
            
            while len(higher_list) > higher_target_len:
                num = higher_list.pop(0)
                higher_sum -= num
                lower_list.add(num)
                lower_sum += num
            
            while lower_list[-1] > higher_list[0]:
                b = lower_list.pop(-1)
                lower_sum -= b
                higher_list.add(b)
                higher_sum += b

                h = higher_list.pop(0)
                higher_sum -= h
                lower_list.add(h)
                lower_sum += h
            # print(lower_list, lower_sum, higher_list, higher_sum, target)
            ops.append(higher_sum - target * len(higher_list) + target * len(lower_list) - lower_sum)

            if lower_list.count(nums[i - window_size + 1]) > 0:
                lower_list.remove(nums[i - window_size + 1])
                lower_sum -= nums[i - window_size + 1]
            else:
                higher_list.remove(nums[i - window_size + 1])
                higher_sum -= nums[i - window_size + 1]
        return ops

    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        medians = self.get_median(nums, x)
        # print(medians)
        ops = self.get_ops(nums, x, medians)
        n = len(ops)
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [float('inf')] * (n + 1)
            for i in range(n - 1, -1, -1):
                take = ops[i] + prev[min(i + x, n)]
                skip = curr[i + 1] if i + 1 <= n else float('inf')
                curr[i] = min(take, skip)
            prev = curr

        return prev[0]
