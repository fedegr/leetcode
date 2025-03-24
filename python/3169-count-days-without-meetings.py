from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        new_meetings = [meetings[0]]
        for i in range(1, len(meetings)):
            if new_meetings[-1][1] < meetings[i][0]:
                new_meetings.append(meetings[i])
            elif new_meetings[-1][1] < meetings[i][1]:
                new_meetings[-1][1] = meetings[i][1]
        
        previous_day_without_meetings = 1
        days_without_meetings = 0
        for s, e in new_meetings:
            days_without_meetings += s - previous_day_without_meetings
            previous_day_without_meetings = e + 1
        
        days_without_meetings += days - previous_day_without_meetings + 1

        return days_without_meetings
