from collections import Counter


def num_tiles(tiles_count, possibilities):
    keys = tuple(k*v for k, v in sorted(tiles_count.items()) if v > 0)
    
    if len(keys) == 1 and tiles_count[keys[0]] == 1:
        possibilities[keys[0]] = 1
        return 1

    key = ''.join(keys)
    if key in possibilities:
        return possibilities[key]

    possibilities[key] = 0
    for k, v in tiles_count.items():
        if v < 1:
            continue
        tiles_count[k] -= 1
        possibilities[key] += num_tiles(tiles_count, possibilities)
        tiles_count[k] += 1
    
    return possibilities[key]



class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        possibilities = {}
        num_tiles(Counter(tiles), possibilities)
        return sum(v for v in possibilities.values())
