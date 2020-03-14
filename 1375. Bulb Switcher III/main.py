class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        res = 0
        s = 0
        for i in range(len(light)):
            s += light[i]
            if s == (i+1)*(i+2) // 2:
                res += 1
        
        return res
