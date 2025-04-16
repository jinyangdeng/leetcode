"""
Original question: https://leetcode.com/problems/count-good-triplets-in-an-array
Needs a clever way to transform the problem.
The nums1_mapped_to_nums2_indices is the most important.
"""

from typing import List
from sortedcontainers import SortedList


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        value_to_index_in_nums2 = {val: idx for idx, val in enumerate(nums2)}
        nums1_mapped_to_nums2_indices = [value_to_index_in_nums2[val] for val in nums1]

        num_xs = []
        seen_left = SortedList()
        for index_in_nums2 in nums1_mapped_to_nums2_indices:
            num_xs.append(seen_left.bisect_left(index_in_nums2))
            seen_left.add(index_in_nums2)

        num_ys = []
        seen_right = SortedList()
        for index_in_nums2 in reversed(nums1_mapped_to_nums2_indices):
            num_ys.append(len(seen_right) - seen_right.bisect_left(index_in_nums2))
            seen_right.add(index_in_nums2)
        num_ys.reverse()

        return sum(num_x * num_y for num_x, num_y in zip(num_xs, num_ys))
