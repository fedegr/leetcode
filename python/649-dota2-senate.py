from collections import deque, Counter


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        oposition = {'R': 'D', 'D': 'R'}
        party_name = {'R': 'Radiant', 'D': 'Dire'}
        bans = {'R': 0, 'D': 0}
        active_members = Counter(senate)
        senate = deque(senate)

        while len(senate) > 0:
            party = senate.popleft()
            if bans[party] > 0:
                bans[party] -= 1
            else:
                active_members[oposition[party]] -= 1
                if active_members[oposition[party]] <= 0:
                    return party_name[party]
                bans[oposition[party]] += 1
                senate.append(party)
            