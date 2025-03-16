"""
Original question: https://leetcode.com/problems/longest-common-prefix-of-k-strings-after-removal
"""
from typing import List


class Trie:
    def __init__(self):
        self.count = 0
        self.bestPrefixLength = 0
        self.nodes = {}

    def update(self, delta: int, word: str, k: int) -> int:
        curr = self
        path = [self]
        for char in word:
            if char not in curr.nodes:
                curr.nodes[char] = Trie()
            curr = curr.nodes[char]
            path.append(curr)
            curr.count += delta

        N = len(path)
        path.reverse()
        for idx, node in enumerate(path):
            cand = (N - idx - 1) if node.count >= k else 0
            for childKey in node.nodes:
                cand = max(cand, node.nodes[childKey].bestPrefixLength)
            node.bestPrefixLength = cand

        return self.bestPrefixLength

class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        if len(words) < k + 1:
            return [0] * len(words)

        root = Trie()
        for word in words:
            root.update(1, word, k)

        res = []
        for word in words:
            res.append(root.update(-1, word, k))
            root.update(1, word, k)

        return res