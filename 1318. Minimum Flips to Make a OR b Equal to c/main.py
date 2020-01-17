class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        for i in range(32):
            x, y, z = (a >> i) & 1, (b >> i) & 1, (c >> i) & 1
            if z==0 and (x+y) >= 1:
                res += (x+y)
            elif z==1 and (x+y) == 0:
                res += 1
        return res
