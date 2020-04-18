class Solution:
    def numOfWays(self, n: int) -> int:
        c3, c2 = 6, 6
        p = 10 ** 9 + 7
        t = 0
        for i in range(2, n+1):
            t = c3
            c3 = (2 * c3 + 2 * c2) % p
            c2 = (2 * t + 3 * c2) % p
        res = (c3 + c2) % p
        return res
