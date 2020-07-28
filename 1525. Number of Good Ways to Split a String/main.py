class Solution:
    def check(self, d1, d2):
        c1 = 0
        c2 = 0
        for c in 'abcdefghijklmnopqrstuvwxyz':
            if d1[c] != 0:
                c1 += 1
            if d2[c] != 0:
                c2 += 1
        return c1 == c2
    
    def numSplits(self, s: str) -> int:
        n = len(s)
        res = 0
        d2 = collections.Counter(s)
        d1 = collections.defaultdict(int)
        for i in range(1, n):
            c = s[i-1]
            d1[c] += 1
            d2[c] -= 1
            if self.check(d1, d2):
                res += 1
        return res
