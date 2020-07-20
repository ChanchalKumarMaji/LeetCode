class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        f = numBottles
        e = 0
        res = 0
        while True:
            res += f
            e += f
            f = e // numExchange
            e -= f*numExchange
            if f == 0:
                break
        return res
