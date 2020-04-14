from collections import defaultdict

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        d = defaultdict(int)
        res = []
        p = [i+1 for i in range(m)]
        for i in range(len(queries)):
            for j in range(m):
                if p[j] == queries[i]:
                    res.append(j)
                    p[:] = [p[j]] + p[:j] + p[j+1:]
                    break
        return res
