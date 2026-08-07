from bisect import bisect_left

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        intervals = self.intervals
        i = bisect_left(intervals, [value + 1])

        if i and intervals[i - 1][1] >= value:
            return

        left = i and intervals[i - 1][1] + 1 == value
        right = i < len(intervals) and intervals[i][0] - 1 == value

        if left and right:
            intervals[i - 1][1] = intervals[i][1]
            intervals.pop(i)
        elif left:
            intervals[i - 1][1] = value
        elif right:
            intervals[i][0] = value
        else:
            intervals.insert(i, [value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
