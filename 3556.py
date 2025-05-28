"""
Original question: https://leetcode.com/problems/sum-of-largest-prime-substrings
"""

import heapq

class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        def isPrime(num):
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        

        h = []
        tested = set()
        N = len(s)
        for left in range(N):
            for right in range(left + 1, N + 1):
                num = int(s[left:right])
                if num in tested:
                    continue
                tested.add(num)
                if isPrime(num):
                    heapq.heappush(h, num)
                if len(h) > 3:
                    heapq.heappop(h)
        
        return sum(h)


        