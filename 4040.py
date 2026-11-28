"""
Original question: https://leetcode.com/problems/minimum-operations-to-form-subset-sum-i
我天，现在 medium 都要用 tabulation 了 💀 (memoization 会 TLE)
"""


class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        # pre compute
        N = len(nums)
        reachable_values_master = [[] for _ in range(N)]
        for idx, num in enumerate(nums):
            reachable_values = [[0, 0]]
            num1 = num
            step = 0
            while num1 >= 2:
                num1 = num1 // 2
                step += 1
                if num1 <= sum:
                    reachable_values.append([num1, step])

            num1 = num
            step = 0
            while num1 <= sum:
                reachable_values.append([num1, step])
                num1 *= 2
                step += 1

            reachable_values.sort()
            reachable_values_master[idx] = reachable_values

        dp = [0] + [float('inf')] * sum
        for reachable_values in reachable_values_master:
            new = dp[:]
            for starting in range(0, sum + 1):
                if dp[starting] == float('inf'):
                    continue
                for reachable_value, steps_needed in reachable_values:
                    if starting + reachable_value > sum:
                        break
                    new[starting + reachable_value] = min(new[starting + reachable_value], dp[starting] + steps_needed)
            dp = new

        return -1 if dp[-1] == float('inf') else dp[-1]
        # @lru_cache(maxsize = None)
        # def dp(idx, sum_remaining):
        #     res = float('inf')
        #     if sum_remaining == 0:
        #         return 0
        #     if idx < 0:
        #         return res

        #     num = nums[idx]
        #     arrivable_values = reachable_values_master[idx]
        #     for reachable_value, steps_needed in arrivable_values:
        #         if reachable_value > sum_remaining:
        #             break
        #         outcome = dp(idx - 1, sum_remaining - reachable_value)
        #         if outcome != float('inf'):
        #             res = min(res, steps_needed + outcome)

        #     return res

        # res = dp(len(nums) - 1, sum)
        # return -1 if res == float('inf') else res