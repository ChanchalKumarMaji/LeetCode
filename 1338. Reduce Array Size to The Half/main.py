from collections import defaultdict

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = defaultdict(int)
        for e in arr:
            d[e] += 1
        res = []
        for k in d:
            res.append(d[k])
        res.sort(reverse = True)
        print(res)
        c = 0
        for i in range(len(res)):
            c += res[i]
            if c >= len(arr) // 2:
                break
        return i+1
