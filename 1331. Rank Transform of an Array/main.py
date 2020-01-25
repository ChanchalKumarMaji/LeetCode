from collections import defaultdict

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        d = defaultdict(int)
        l = sorted(set(arr))
        for i in range(len(l)):
            d[l[i]] = i+1
        return [d[e] for e in arr]
