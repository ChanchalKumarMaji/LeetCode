from collections import defaultdict

class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = {}
        t = set()
        res = []
        for order in orders:
            name, tn, fi = order
            tn = int(tn)
            t.add(fi)
            if tn not in d:
                d[tn] = {}
            if fi not in d[tn]:
                d[tn][fi] = 1
            else:
                d[tn][fi] += 1
        t = list(t)
        t.sort()
        p = {}
        for i in range(len(t)):
            p[t[i]] = i + 1
        res.append(["Table"] + t)
        for tn in sorted(d):
            t = ["0"] * len(res[0])
            t[0] = str(tn)
            for k in d[tn]:
                t[p[k]] = str(d[tn][k])
            res.append(t)
        return res
