class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < res[-1][1]:
                if interval[1] < res[-1][1]:
                    res.pop()
                    res.append(interval)
            else:
                res.append(interval)

        return len(intervals) - len(res)