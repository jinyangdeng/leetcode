"""
Original question: https://leetcode.com/problems/resulting-string-after-adjacent-removals
"""

from collections import deque


class Solution:
    def resultingString(self, s: str) -> str:
        left = []
        right = deque(s)

        while right:
            char = right.popleft()
            if left and abs(ord(left[-1]) - ord(char)) in [1, 25]:   
                left.pop()
            else:
                left.append(char)
        
        return ''.join(left)
    