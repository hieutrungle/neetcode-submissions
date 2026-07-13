"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq 

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        heap = []
        intervals.sort(key= lambda x: x.start)
        res = 0

        for interval in intervals:
            while heap and heap[0] <= interval.start:
                heapq.heappop(heap)
            heapq.heappush(heap, interval.end)
            res = max(res, len(heap))

        return res