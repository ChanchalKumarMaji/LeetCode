from collections import defaultdict

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = defaultdict(int)
        for i in range(1, 1000+1):
            n = i
            c = 0
            while (n != 1) and (n not in d):
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = n * 3 + 1
                c += 1
            d[i] = c + d[n]
        #print(d)
        res = []
        for i in range(lo, hi+1):
            res.append((d[i], i))
        res.sort()
        return res[k-1][1]
