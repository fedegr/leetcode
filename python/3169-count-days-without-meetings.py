class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        # agenda = [0] * (days + 2)
        # for s, e in meetings:
        #     agenda[s] += 1
        #     agenda[e+1] -= 1
        
        # days_without_meetings = 0
        # meetings_count = 0
        # for i in range(1, days+1):
        #     meetings_count += agenda[i]
        #     if meetings_count == 0:
        #         days_without_meetings += 1

        # return days_without_meetings

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
