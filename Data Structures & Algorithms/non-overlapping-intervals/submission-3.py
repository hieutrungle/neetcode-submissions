class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        cur = intervals[0][1]
        cnt = 0
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] < cur:
                if interval[1] < cur:
                    cur = interval[1]
                cnt += 1
            else:
                cur = interval[1]

        return cnt