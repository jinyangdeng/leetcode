"""
Original question: https://leetcode.com/problems/eat-pizzas The trick is that given W ≤ X ≤ Y ≤ Z, where you are
taking Z on odd days and Y on even days. W and X are not important at all. They will always come from the smaller
half. Disregard them. Now, you look at the bigger half, where Y and Z will come from.

You don't want to sacrifice any opportunity to take Z. So you count the number of odd days, and spent them taking the
biggest ones. Then on even days, you take whatever is remaining, form pairs of (Y,Z)s, then take the Ys.
"""

from typing import List


class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        pizzas.sort()
        n = len(pizzas)
        days = n // 4
        num_odd_numbered_days = (days + 1) // 2
        num_even_numbered_days = days - num_odd_numbered_days

        return sum(pizzas[n - num_odd_numbered_days:]) + sum(
            pizzas[n - num_odd_numbered_days - 2 * num_even_numbered_days:n - num_odd_numbered_days:2])
