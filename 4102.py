"""
Original question: https://leetcode.com/problems/count-valid-substrings-i
很容易弄错
因为 xxx abc yyy
xxx ab 得在 c 之前结束，而
bc yyy 得在 a 之后开始
因此很容易 double count b 本身
"""


class Solution:
    def countValidSubstrings(self, s: str) -> int:
        N = len(s)
        abc_c_locations = []

        for i in range(N - 2):
            if s[i:i+3] == "abc":
                abc_c_locations.append(i+2)
        
        # There is at least 1 abc divider
        res = 0
        starting_position = 0
        for val in abc_c_locations:
            # In front all can reach until b (inclusive)
            effectiveLength = (val - starting_position)
            res += (effectiveLength * (effectiveLength +1) // 2)
            
            # except for b itself 
            res -= 1
            # because my next starting position is b 
            starting_position = val - 1
        
        res += ((N - starting_position) * (N - starting_position + 1)) // 2

        return res

"""
一看 Lee215 的解释，简直是神人啊
def countValidSubstrings(self, s: str) -> int:
    res = -s.count('abc')
    for p in s.replace('abc', 'ab bc').split():
        res += len(p) * (len(p) + 1) // 2
    return res
这个 -s.count("abc") 和 -1 （for b) 有异曲同工之妙
"""