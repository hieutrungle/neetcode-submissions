class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        cur = intervals[0]
        cnt = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < cur[1]:
                if interval[1] < cur[1]:
                    cur = interval
                cnt += 1
            else:
                cur = interval

        return cnt