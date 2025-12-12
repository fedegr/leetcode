from collections import deque

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        answer = [0] * numberOfUsers
        online_users = set(i for i in range(numberOfUsers))
        offline_users = deque()
        
        sorted_events = sorted(
            map(lambda x: (x[0], int(x[1]), x[2]), events), 
            key=lambda x: (x[1], 0 if x[0] == "OFFLINE" else 1)
        )

        all_mentions = 0
        for kind, timestamp, value in sorted_events:
            while len(offline_users) > 0 and offline_users[0][1] <= timestamp:
                user, _ = offline_users.popleft()
                online_users.add(user)
            
            if kind == "OFFLINE":
                user_id = int(value)
                online_users.remove(user_id)
                offline_users.append((user_id, timestamp + 60))
            else:
                if value == "ALL":
                    all_mentions += 1
                elif value == "HERE":
                    for user_id in online_users:
                        answer[user_id] += 1
                else:
                    for user in value.split():
                        user_id = int(user[2:])
                        answer[user_id] += 1
        
        return [
            (x + all_mentions)
            for x in answer
        ]
