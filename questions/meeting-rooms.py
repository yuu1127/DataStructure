class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        #intervals.sort(key=lambda x: x.start)
        intervals.sort(key=lambda x: x[0])
        print(intervals)
        for i in range(1, len(intervals)):
            print(intervals[i])
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True
