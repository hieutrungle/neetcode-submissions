class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= res[-1][1]:
                res[-1][0] = min(res[-1][0], interval[0])
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res