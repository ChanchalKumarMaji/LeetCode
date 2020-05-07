class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        d = [int(c) for c in num]
        d = list(set(d))
        res = []
        for x in d:
            for y in range(0, 10):
                p = str(num)
                p = p.replace(str(x), str(y))
                if p[0] != '0' and int(p) != 0:
                    res.append(int(p))
        res = list(set(res))
        res.sort()
        #print(res)
        return res[-1] - res[0]
