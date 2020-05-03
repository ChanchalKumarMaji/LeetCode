from collections import defaultdict

class Solution:
    def countLargestGroup(self, n: int) -> int:
        d = defaultdict(int)
        for i in range(1, n+1):
            s = sum([int(e) for e in str(i)])
            d[s] += 1
        l = list(d.values())
        return l.count(max(l))
