"""
Original question: https://leetcode.com/problems/number-of-stable-subsequences
"""
from typing import List

class Solution:
    def countStableSubsequences(self, nums: List[int]) -> int:
        MOD = 1_000_000_007
        odd = [0, 0]
        even = [0, 0]
        
        for num in nums:            
            if num % 2:  
                odd[0], odd[1] = (odd[0] + 1 + even[0] + even[1])%MOD, (odd[1] + odd[0])%MOD
            else:        
                even[0], even[1] = (even[0] + 1 + odd[0] + odd[1])%MOD, (even[1] + even[0])%MOD
        
        return (sum(odd) + sum(even)) % MOD
