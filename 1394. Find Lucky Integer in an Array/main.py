from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d = Counter(arr)
        res = [-1]
        for k in d:
            if k == d[k]:
                res.append(k)
        return max(res)
