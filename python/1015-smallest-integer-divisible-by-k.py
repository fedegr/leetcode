class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        last = 1 % k
        mods = {last}
        while last != 0:
            last = (last * 10 + 1) % k
            if last in mods:
                return -1
            mods.add(last)
        
        return len(mods)
