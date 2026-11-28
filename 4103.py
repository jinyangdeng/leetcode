"""
Original question: https://leetcode.com/problems/remove-elements-by-type-and-color
这个题目的描述非常模糊，比如
1. Groupsize 里的 element 能不能重复用来删 type & color? (这题是可以的)
So types = [0, 0, 0, 0], colors = [2, 2, 1, 1], groupSize = [2] 是可以的
1b. 同时，groupSize 里的 element 是不是要都用一遍？（这题是不需要的）
So types = [0, 0, 0, 0], colors = [2, 2, 1, 1], groupSize = [2， 100] 也是可以的
2. Groupsize 里的 operation，需不需要根据顺序使用？（这题是不需要的）
"""


class Solution:
    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
        # Each element in the stack is [type, color, count]
        stack = []

        for t, c in zip(types, colors):
            if stack and stack[-1][:2] == [t, c]:
                stack[-1][2] += 1
            else:
                stack.append([t, c, 1])
        
            if stack[-1][2] == groupSize[t]:
                stack.pop()
        
        return not stack
