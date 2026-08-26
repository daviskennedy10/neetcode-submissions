"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        
        n = len(intervals)
        if n <= 1:
            return True
        prev = intervals[0]
        for i in range(1,n):
            start = intervals[i].start
            end = intervals[i].end
            pstart = prev.start
            pend = prev.end
            if start < pend:
                return False
            prev = intervals[i]
        return True
