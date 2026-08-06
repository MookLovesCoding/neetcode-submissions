"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        newIntervals = sorted(intervals, key = lambda i: i.start)
        for i in range(1, len(newIntervals)):
            if newIntervals[i].start < newIntervals[i - 1].end:
                return False
        return True