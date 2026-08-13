"""
Original question: https://leetcode.com/problems/peaks-in-array-ii
"""
from sortedcontainers import SortedList

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[2 * index] + self.tree[2 * index + 1]

    def query(self, left, right):
        left += self.n
        right += self.n
        result = 0
        while left < right:
            if left % 2 == 1:
                result += self.tree[left]
                left += 1
            if right % 2 == 1:
                right -= 1
                result += self.tree[right]
            left //= 2
            right //= 2
        return result
    
    def debug(self):
        print(self.tree[self.n:])

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        peaks = []
        for idx in range(1, len(nums) - 1):
            if nums[idx - 1] < nums[idx] > nums[idx + 1]:
                peaks.append(idx)
        
        leftFlexibility = [0] * len(nums)
        lastSeen = 0
        for p in peaks:
            leftFlexibility[p] = p - lastSeen 
            lastSeen = p

        rightFlexibility = [0] * len(nums)
        for p in peaks:
            rightFlexibility[p] = len(nums) - p - 1

        peaks = SortedList(peaks)

        numSubArrays = SegmentTree([left * right for left, right in zip(leftFlexibility, rightFlexibility)])
        leftFlexSum = SegmentTree(leftFlexibility)

        # print(leftFlexibility)
        # print(rightFlexibility)
        # numSubArrays.debug()
        # leftFlexSum.debug()      

        # print("START PROCESSING")
        res = []
        for qType, x, y in queries:
            if qType == 1:
                l, r = x, y
                closestPeakIdxOnRight = peaks.bisect_left(l + 1)
                if closestPeakIdxOnRight == len(peaks) or peaks[closestPeakIdxOnRight] >= r:
                    res.append(0)
                    continue
                closestPeakOnRight = peaks[closestPeakIdxOnRight]
                numSubArray = numSubArrays.query(closestPeakOnRight, r)
                numSubArray -= (leftFlexibility[closestPeakOnRight] - (closestPeakOnRight - l))* rightFlexibility[closestPeakOnRight]
                # print(numSubArray, (len(nums) - r - 1), leftFlexSum.query(l + 1, r))
                # 是 query l + 1, r 而不是 query l, r (因为 l 本身可能是 peak)
                numSubArray -= (len(nums) - r - 1) * (leftFlexSum.query(l + 1, r) -  (leftFlexibility[closestPeakOnRight] - (closestPeakOnRight - l)))
                res.append(numSubArray)
            else:
                idx, val = x, y
                # Need to update nums, peaks, leftFlexibility, rightFlexibility, numSubArrays, leftFlexSum
                nums[idx] = val
                newPeaks = []
                noLongerPeaks = []
                # print(peaks)
                for i in [idx - 1, idx, idx + 1]:
                    if i in peaks and not (nums[i - 1] < nums[i] > nums[i + 1]):
                        noLongerPeaks.append(i)
                    elif i not in peaks and 0 < i < len(nums) - 1 and (nums[i - 1] < nums[i] > nums[i + 1]):
                        newPeaks.append(i)

                for newPeak in newPeaks:
                    peaks.add(newPeak)
                    leftFlexibility[newPeak] = newPeak - (peaks[peaks.index(newPeak) - 1] if peaks.index(newPeak) > 0 else newPeak)
                    if peaks.index(newPeak) + 1 < len(peaks):
                        nextPeak = peaks[peaks.index(newPeak) + 1]
                        leftFlexibility[nextPeak] = nextPeak - newPeak
                        numSubArrays.update(nextPeak, leftFlexibility[nextPeak] * rightFlexibility[nextPeak])
                        leftFlexSum.update(nextPeak, leftFlexibility[nextPeak])

                    rightFlexibility[newPeak] = len(nums) - newPeak - 1
                    numSubArrays.update(newPeak, leftFlexibility[newPeak] * rightFlexibility[newPeak])
                    leftFlexSum.update(newPeak, leftFlexibility[newPeak])

                # print(newPeaks, noLongerPeaks)
                # print(leftFlexibility)
                # print(rightFlexibility)
                # numSubArrays.debug()
                # leftFlexSum.debug()      

                for oldPeak in noLongerPeaks:
                    loc = peaks.index(oldPeak)
                    peaks.remove(oldPeak)
                    leftFlexibility[oldPeak] = 0
                    # 是 loc 而非 loc + 1 因为我们已经删除了 oldPeak
                    if loc < len(peaks):
                        nextPeak = peaks[loc]
                        leftFlexibility[nextPeak] = nextPeak - (peaks[loc - 1] if loc > 0 else nextPeak)
                        numSubArrays.update(nextPeak, leftFlexibility[nextPeak] * rightFlexibility[nextPeak])
                        leftFlexSum.update(nextPeak, leftFlexibility[nextPeak])

                    rightFlexibility[oldPeak] = 0
                    numSubArrays.update(oldPeak, 0)
                    leftFlexSum.update(oldPeak, 0)

                # print(newPeaks, noLongerPeaks)
                # print(leftFlexibility)
                # print(rightFlexibility)
                # numSubArrays.debug()
                # leftFlexSum.debug()                
        return res