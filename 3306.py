"""
Original question: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii
Initially, I thought it is like:
for each position, add up the max(0, k+1_consonant_later - max(k_consonant_later, next_a, next_e ... ))

However, this is flawed, because when word = "aeioua", k = 0, the above approach will fail.

Question suggested binary search, but times out. Hence, sliding window is the way to go.
"""


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowel_count = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        consonant_count = 0
        res = 0

        left = 0
        left_count = 0
        for right, char in enumerate(word):
            if char in vowel_count:
                vowel_count[char] += 1
            else:
                consonant_count += 1
                left_count = 0

            while k < consonant_count and left < right:
                if word[left] in vowel_count:
                    vowel_count[word[left]] -= 1
                else:
                    consonant_count -= 1
                left += 1

            while k == consonant_count and all(val > 0 for val in vowel_count.values()):
                if word[left] in vowel_count:
                    vowel_count[word[left]] -= 1
                else:
                    consonant_count -= 1
                left += 1
                left_count += 1

            res += left_count

        return res
