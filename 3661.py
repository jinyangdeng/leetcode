"""
Original question: https://leetcode.com/problems/maximum-walls-destroyed-by-robots
AI failed to come up with a working solution on its own.
I have to come up with a top-down memoization approach (which is sufficient to pass all tests).
But AI managed to convert it to a bottom-up approach (which is more memory-efficient).
"""

import bisect
from typing import List

# from functools import lru_cache
# class Solution:
#     def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
#         walls.sort()
#         mix = [(r, d) for r, d in zip(robots, distance)]
#         mix.sort()
#         robots = [e[0] for e in mix]
#         distance = [e[1] for e in mix]
#
#         @lru_cache(None)
#         def dp(robot_idx, prev_robot_move_left):
#             if robot_idx >= len(robots): return 0
#             robot_pos = robots[robot_idx]
#             # Originally, you can move distance[robotIdx]
#             left_left, left_right = robots[robot_idx] - distance[robot_idx], robots[robot_idx]
#             right_left, right_right = robots[robot_idx], robots[robot_idx] + distance[robot_idx]
#
#             # If there is robot to my left
#             if robot_idx > 0:
#                 prev_robot_pos = robots[robot_idx - 1]
#                 # I cannot infringe the previous robot's position
#                 left_left = max(left_left, prev_robot_pos + 1)
#
#                 # And that robot moved right
#                 if not prev_robot_move_left:
#                     prev_robot_right_right = prev_robot_pos + distance[robot_idx - 1]
#                     left_left = max(left_left, prev_robot_right_right + 1)
#
#             # If there is robot to my right
#             if robot_idx < len(robots) - 1:
#                 next_robot_pos = robots[robot_idx + 1]
#                 # I cannot infringe the next robot's position
#                 right_right = min(right_right, next_robot_pos - 1)
#
#             left_walls = max(0, bisect.bisect_left(walls, left_right + 1) - bisect.bisect_left(walls, left_left))
#             right_walls = max(0, bisect.bisect_left(walls, right_right + 1) - bisect.bisect_left(walls, right_left))
#
#             return max(
#                 left_walls + dp(robot_idx + 1, True),
#                 right_walls + dp(robot_idx + 1, False),
#             )
#
#         numRobots = len(robots)
#         return max(dp(0, True), dp(numRobots - 1, False))

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # Preprocess: sort walls; sort robots together with their distances by position
        walls.sort()
        order = sorted(range(len(robots)), key=lambda i: robots[i])
        robots = [robots[i] for i in order]
        distance = [distance[i] for i in order]

        n = len(robots)

        dp = [0, 0]

        # helper to count walls in [L, R]
        def count_walls(L: int, R: int) -> int:
            if L > R:
                return 0
            return max(0, bisect.bisect_left(walls, R + 1) - bisect.bisect_left(walls, L))

        for i in range(n - 1, -1, -1):
            rpos = robots[i]
            dist_i = distance[i]

            # Right move interval (doesn't depend on prev move; only on next robot position)
            right_L = rpos
            right_R = rpos + dist_i
            if i < n - 1:
                right_R = min(right_R, robots[i + 1] - 1)
            right_walls = count_walls(right_L, right_R)
            new = [0, 0]
            # For each prev-move state: compute left interval & transition
            for prev_moved_left in (0, 1):  # 0=False, 1=True
                # Left move base interval
                left_L = rpos - dist_i
                left_R = rpos

                if i > 0:
                    prev_pos = robots[i - 1]
                    left_L = max(left_L, prev_pos + 1)  # cannot infringe previous robot's position
                    if prev_moved_left == 0:
                        # previous moved right: its occupied rightmost position expands blocking area
                        left_L = max(left_L, prev_pos + distance[i - 1] + 1)

                left_walls = count_walls(left_L, left_R)

                take_left = left_walls + dp[1]
                take_right = right_walls + dp[0]

                new[prev_moved_left] = max(take_left, take_right)
            dp = new

        # Start with no previous robot; either assumption on "previous moved left" is fine—take the better.
        return max(dp)
