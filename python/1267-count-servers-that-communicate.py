from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        servers = {'x': {}, 'y': {}}
        for y, row in enumerate(grid):
            for x, s in enumerate(row):
                if s == 0:
                    continue
                servers['y'].setdefault(y, set()).add((x,y))
                servers['x'].setdefault(x, set()).add((x,y))

        connected = set()
        for lines in servers.values():
            for connections in lines.values():
                if len(connections) == 1:
                    continue
                connected.update(connections)
        
        return len(connected)
