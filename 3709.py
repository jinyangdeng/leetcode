"""
Original question: https://leetcode.com/problems/design-exam-scores-tracker
"""
import bisect

class ExamTracker:

    def __init__(self):
        self.scores = [(0, 0)]

    def record(self, time: int, score: int) -> None:
        self.scores.append((time, self.scores[-1][1] + score))

    def totalScore(self, startTime: int, endTime: int) -> int:
        leftIdx = bisect.bisect_left(self.scores, (startTime, 0)) - 1
        rightIdx = bisect.bisect_left(self.scores, (endTime, float('inf'))) - 1

        return self.scores[rightIdx][1] - self.scores[leftIdx][1]


# Your ExamTracker object will be instantiated and called as such:
# obj = ExamTracker()
# obj.record(time,score)
# param_2 = obj.totalScore(startTime,endTime)