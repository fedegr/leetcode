class Solution:
    def countCollisions(self, directions: str) -> int:
        crashes = 0
        prev_stop = False
        going_right = 0
        for i, d in enumerate(directions):
            if d == "R":
                going_right += 1
                prev_stop = False
            elif d == "S":
                crashes += going_right
                going_right = 0
                prev_stop = True
            elif d == "L":
                if prev_stop:
                    crashes += 1
                elif going_right > 0:
                    crashes += going_right + 1
                    going_right = 0
                    prev_stop = True
            # print(f'{i:03}', d, crashes)
            
        return crashes
