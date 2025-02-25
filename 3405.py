"""
Original question: https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements
It's essentially a math problem

Example: n=6,k=2
We represent the array using:
'x' → a number different from the previous number.
'o' → a number same as the previous number.

Examples of valid arrays:
x x o o x x
x x o x o x
x o x x x o

To better understand, we can think of these arrays as being divided into compartments where:
# Within a compartment, the numbers are the same.
# Between adjacent compartments, the numbers are different.

Visualizing compartments:
x x o o x x → | x | x o o | x | x |
x x o x o x → | x | x o | x o | x |
x o x x x o → | x o | x | x | x o |

Step 1: Counting Ways to Assign Numbers to Compartments
# The first compartment (starting number) has m choices. 
# Every other compartment (where a new number is assigned) has (m - 1) choices since it must be different from the previous compartment.
Thus, the total number of ways to assign numbers to the compartments is: m * (m - 1) ** (n - k - 1)

Step 2: Choosing the Placement of 'o's
The 'o's represent positions where the value is the same as the previous one. They can be placed anywhere except at index 0.
We have (n - 1) possible positions to place these 'o's. We must choose exactly k positions for them. So (n - 1) choose k
"""

import math

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1_000_000_007
        return m * pow(m - 1, n - k - 1, MOD) * math.comb(n - 1, k) % MOD