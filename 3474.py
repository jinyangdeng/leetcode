"""
Original question: https://leetcode.com/problems/lexicographically-smallest-generated-string
I thought it was KMP. Turns out O(len(str1) * len(str2)) works.
"""

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = ["a"] * (n + m - 1)

        immutable_indices = set()
        for i in range(n):
            if str1[i] == "T":
                for j in range(m):
                    immutable_indices.add(i + j)
                    res[i + j] = str2[j]

        for i in range(n):
            is_match = True
            for j in range(m):
                if res[i + j] != str2[j]:
                    is_match = False
                    break

            if str1[i] == "T":
                if is_match:
                    continue
                else:
                    return ""

            if is_match:
                is_fixed = False
                for j in range(m - 1, -1, -1):
                    if i + j in immutable_indices:
                        continue
                    res[i + j] = "b"
                    is_fixed = True
                    break

                if not is_fixed:
                    return ""
        return ''.join(res)