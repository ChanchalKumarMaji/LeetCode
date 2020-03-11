from collections import Counter

class Solution:
    def sortString(self, s: str) -> str:
        d = Counter(s)
        asc = True
        res = ""
        while d:
            for k in sorted(d.keys()) if asc else reversed(sorted(d.keys())):
                res += k
                d[k] -= 1
                if d[k] == 0:
                    del d[k]
            asc = not asc
        
        return res
