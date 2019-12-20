class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        ans = []
        for i in range(1, 10):
            t = i
            res.append(t)
            while t % 10 < 9:
                t = t * 10 + (t % 10 + 1)
                res.append(t)
        
        for e in res:
            if low <= e <= high:
                ans.append(e)
        
        ans.sort()
        
        return ans
