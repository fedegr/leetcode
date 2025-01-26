from collections import deque 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        window_count = {}
        window = deque()
        cover = 0
        best_window = None
        for i, c in enumerate(s):
            if c not in count_t:
                continue
            
            window_count[c] = window_count.get(c, 0) + 1
            window.append(i)
            if window_count[c] <= count_t[c]:
                cover += 1

            start = s[window[0]]
            while window_count[start] > count_t[start]:
                window.popleft()
                window_count[start] -= 1
                start = s[window[0]]
            
            if cover == len(t) and (best_window is None or (window[-1] - window[0])  < (best_window[-1] - best_window[0])):
                best_window = (window[0], window[-1])

        return s[best_window[0]:best_window[-1]+1] if best_window is not None else ""
    