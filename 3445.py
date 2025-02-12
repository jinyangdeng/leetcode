from math import inf

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        chars = ['0', '1', '2', '3', '4']

        res = -inf
        for oddChar in chars:
            for evenChar in chars:
                if oddChar == evenChar:
                    continue

                oddCharCount, evenCharCount = 0, 0
                helper = {(oddCharCount % 2, evenCharCount % 2): 0}

                left = 0
                leftOddCharCount, leftEvenCharCount = 0, 0
                for right, char in enumerate(s):
                    oddCharCount += char == oddChar
                    evenCharCount += char == evenChar

                    while ((right - left >= k)
                           and not (s[left] == oddChar and oddCharCount - leftOddCharCount <= 1)
                           and not (s[left] == evenChar and evenCharCount - leftEvenCharCount <= 2)):
                        leftOddCharCount += s[left] == oddChar
                        leftEvenCharCount += s[left] == evenChar
                        helper[(leftOddCharCount % 2, leftEvenCharCount % 2)] = min(leftOddCharCount - leftEvenCharCount, helper.get((leftOddCharCount % 2, leftEvenCharCount % 2), inf))
                        left += 1

                    if (right - left >= k - 1) and (oddCharCount - leftOddCharCount >= 1) and (evenCharCount - leftEvenCharCount >= 2):
                        oppositeKey = (1 - oddCharCount % 2, evenCharCount % 2)
                        if oppositeKey in helper:
                            res = max(res, oddCharCount - evenCharCount - helper[oppositeKey])

        return res