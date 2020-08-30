class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.numdisjoint = n

    def find(self, x):
        xp = x
        children = []
        while xp != self.parents[xp]:
            children.append(xp)
            xp = self.parents[xp]
        for c in children:
            self.parents[c] = xp
        return xp

    def union(self, a, b):
        ap = self.find(a)
        bp = self.find(b)
        if ap == bp:
            return

        if self.ranks[ap] < self.ranks[bp]:
            self.parents[ap] = bp
            self.sizes[bp] += self.sizes[ap]
        elif self.ranks[bp] < self.ranks[ap]:
            self.parents[bp] = ap
            self.sizes[ap] += self.sizes[bp]
        else:
            self.parents[bp] = ap
            self.ranks[ap] += 1
            self.sizes[ap] += self.sizes[bp]

        self.numdisjoint -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        arr = [i-1 for i in arr]    # to keep values in range [0, n-1] easy for UFDS
        s = set()
        res = -1
        d = [0] * (len(arr) + 1)
        u = UFDS(len(arr))
        for i, val in enumerate(arr):
            s.add(val)
            if (val > 0) and (val-1 in s):
                d[u.size(val-1)] -= 1
                u.union(val-1, val)
            if (val < len(arr)-1) and (val+1 in s):
                d[u.size(val+1)] -= 1
                u.union(val, val+1)
            d[u.size(val)] += 1
            if d[m] >= 1:
                res = max(res, i+1)
        return res
