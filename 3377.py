"""
Original question: https://leetcode.com/problems/digit-operations-to-make-two-integers-equal/
Rules:
- Choose any digit from n that is not 9 and increase it by 1.
- Choose any digit from n that is not 0 and decrease it by 1.
- NO LEADING ZEROS (they didn't say though), 19 -x-> 09
"""

import heapq
from collections import defaultdict

prime = set([i for i in range(2, 10001)])
for i in range(2, 10001):
    start = i
    while start + i < 10001:
        start += i
        prime.discard(start)


class Solution:
    def minOperations(self, n: int, m: int) -> int:
        if n in prime:
            return -1
        N = len(str(n))

        h = [(n, n)]
        seen = defaultdict(lambda: float('inf'))
        seen[n] = n
        while h:
            currScore, n = heapq.heappop(h)
            if n == m:
                return currScore

            # Go through all the digits, try to +/- 1
            for i in range(N):
                for DIR in [-1, +1]:
                    if str(n)[~i] == '0' and DIR == -1:
                        continue
                    if str(n)[~i] == '9' and DIR == +1:
                        continue
                    newNum = n + DIR * (10 ** i)
                    if len(str(newNum)) != N:
                        continue
                    if newNum not in prime and seen[newNum] > currScore + newNum:
                        seen[newNum] = currScore + newNum
                        heapq.heappush(h, (currScore + newNum, newNum))

        return -1