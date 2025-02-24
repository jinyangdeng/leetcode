"""
Original question: https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square
"""


import bisect
from typing import List

class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        #        1
        #      ____
        #   0 |    | 2
        #     |____|
        #        3

        distances = []

        for px, py in points:
            if px == 0 and 0 <= py < side:
                distances.append(py)
            elif 0 <= px < side and py == side:
                distances.append(side + px - 0)
            elif px == side and 0 < py <= side:
                distances.append(3 * side - py)
            elif 0 < px <= side and py == 0:
                distances.append(4 * side - px)

        distances.sort()

        def works(distance):
            for num in distances:
                start = num
                curr = 1
                idx = bisect.bisect_left(distances, num + distance)
                while idx < len(distances):
                    curr += 1
                    if curr >= k:
                        # I care about the last point
                        if start + 4 * side - distances[idx] >= distance:
                            return True
                        else:
                            break
                    idx = bisect.bisect_left(distances, distances[idx] + distance)
            return False

        left, right = 0, 4 * side
        while left < right:
            mid = (left + right + 1) // 2
            if works(mid):
                left = mid
            else:
                right = mid - 1

        return left