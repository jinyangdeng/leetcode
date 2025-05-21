"""
Original question: https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/
It's a monotically increasing stack question
0 can be used to 'clear' numbers before it, but itself should not be counted
"""
from typing import List

# My solution
# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         res = 0
#         stack = []
#         for num in nums:
#             if len(stack) == 0 and num == 0:
#                 continue

#             if len(stack) == 0 or stack[-1] < num:            
#                 stack.append(num)

#             elif stack[-1] > num:
#                 while stack and stack[-1] > num:
#                     stack.pop()
#                     res += 1
                
#                 if len(stack) == 0 or stack[-1] < num:
#                     if num != 0:
#                         stack.append(num)
        
#         return res + len(stack)

# Good solution: Using a dummy 0 as a starting number
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        stack = [0]
        for num in nums:
            while num < stack[-1]:
                stack.pop()
            if num > stack[-1]:
                ans += 1
            stack.append(num)
        return ans
