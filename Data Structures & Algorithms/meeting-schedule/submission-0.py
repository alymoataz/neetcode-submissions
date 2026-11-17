"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        last_end=0
        intervals.sort(key=lambda i:i.start)
        for i in intervals:
            if i.start<last_end:
                return False
            last_end=i.end
        return True    


