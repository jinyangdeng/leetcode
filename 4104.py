"""
Original question: https://leetcode.com/problems/count-valid-substrings-ii
大幅沿用了 4102.py 的思路
但其实，最好的方法还是从新想
"""


class Solution:
    def countValidSubstrings(self, s: str) -> int:
        N = len(s)
        # 如果是 b ，左边最靠近的 a
        a_loc = None
        nearest_a_on_left_of_b = [None] * N
        for idx, char in enumerate(s):
            if char == 'a':
                a_loc = idx
            if char == 'b':
                nearest_a_on_left_of_b[idx] = a_loc

        # 如果是 c ，左边最靠近的 a (that has a b in the middle)
        b_loc = None
        nearest_a_on_left_of_c = [None] * N
        for idx, char in enumerate(s):
            if char == 'b':
                b_loc = nearest_a_on_left_of_b[idx]
            if char == 'c':
                nearest_a_on_left_of_c[idx] = b_loc
        
        abc_c_locations = [idx for idx, val in enumerate(nearest_a_on_left_of_c) if val != None]
        
        # There is at least 1 abc divider
        res = 0
        starting_position = 0
        for val in abc_c_locations:
            # In front all can reach until 1 char before me (inclusive)
            effectiveLength = (val - starting_position)
            res += (effectiveLength * (effectiveLength +1) // 2)
            res -= ((val - nearest_a_on_left_of_c[val] - 1) * (val - nearest_a_on_left_of_c[val]) // 2)
            # because my next starting position is b 
            starting_position = nearest_a_on_left_of_c[val] + 1

        res += ((N - starting_position) * (N - starting_position + 1)) // 2

        return res

"""
最优解:
class Solution:
    def countValidSubstrings(self, s: str) -> int:
        last_a=-1
        last_ab=-1
        left=-1
        res=0

        for right, char in enumerate(s):
            if char == "a":
                last_a=right
            elif char == "b":
                last_ab=last_a
            else:
                left=last_ab
            
            res += right - left
        
        return res
"""
