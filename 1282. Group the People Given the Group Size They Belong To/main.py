from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for i in range(len(groupSizes)):
            d[groupSizes[i]].append(i)
        res = []
        for k in d.keys():
            v = d[k]
            for i in range(0, len(v), k):
                res.append(v[i:i+k])
        
        return res
