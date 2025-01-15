class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        bits1 = [int(b) for b in format(num1, 'b')]
        bits1count = sum(bits1)

        bits2 = [int(b) for b in format(num2, 'b')]
        bits2count = sum(bits2)

        ans = list(reversed(bits1))
        if bits1count <= bits2count:
            diff = bits2count - bits1count
            
            i = 0
            while diff > 0:
                if i == len(ans):
                    ans.append(1)
                    diff -= 1
                elif ans[i] == 0:
                    ans[i] = 1
                    diff -= 1
                i += 1
        else:
            diff = bits1count - bits2count

            i = 0
            while diff > 0:
                if ans[i] == 1:
                    ans[i] = 0
                    diff -= 1
                i += 1
        
        ans = list(reversed(ans))

        return int(''.join(map(str,ans)), base=2)
