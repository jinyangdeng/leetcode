"""
Original question: https://leetcode.com/problems/longest-special-path-ii
Yes, it's dfs. :)
"""
from typing import List
from collections import defaultdict

class Solution:
    def longestSpecialPath(self, edges: List[List[int]], nums: List[int]) -> List[int]:
        adjList = defaultdict(list)
        for f, t, l in edges:
            adjList[f].append([t, l])
            adjList[t].append([f, l])

        res = [0, 0]

        def dfs(path, lastSeen, lastRepeatIdx, lastLastRepeatIdx):
            nonlocal res
            currNode, currLength, currDepth = path[-1]
            oldLastSeen = lastSeen.get(nums[currNode], None)
            lastSeen[nums[currNode]] = len(path) - 1

            helper = sorted([lastRepeatIdx, lastLastRepeatIdx, oldLastSeen])

            if helper[1] is None:
                myRes = [currLength, currDepth + 1]
            else:
                myRes = [currLength - path[helper[1] + 1][1], currDepth - path[helper[1][1] + 1][2] + 1]

            if myRes[0] > res[0]:
                res = myRes
            elif myRes[0] == res[0]:
                res[1] = min(myRes[1], res[1])

            for nghb, length in adjList[currNode]:
                if len(path) >= 2 and nghb == path[-2][0]:
                    continue
                path.append([nghb, currLength + length, currDepth + 1])
                dfs(path, lastSeen, helper[2][1], helper[1][1])
                path.pop()

            del lastSeen[nums[currNode]]
            if oldLastSeen is not None:
                lastSeen[nums[currNode]] = oldLastSeen

        dfs([[0, 0, 0]], dict(), None, None)
        return res