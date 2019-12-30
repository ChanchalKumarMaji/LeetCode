class Solution:
    def score(self, value):
        res = 0
        for e in self.arr:
            if e > value:
                res += value
            else:
                res += e
        return res
    
    def findBestValue(self, arr: List[int], target: int) -> int:
        self.arr = arr[:]
        l, h = 1, max(arr)
        while l < h:
            m = (l+h) // 2
            if self.score(m) < target:
                l = m + 1
            else:
                h = m
        #print(l, h)        
        s1 = abs(self.score(h-1)-target)
        s2 = abs(self.score(h)-target)
        if s1 <= s2:
            return h-1
        return h
