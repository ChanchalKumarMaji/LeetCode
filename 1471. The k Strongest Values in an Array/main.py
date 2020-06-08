class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        m = sorted(arr)[(n-1)//2]
        #print(m)
        res = []
        for e in arr:
            res.append((abs(e-m), e))
        res.sort(key = lambda x : (-x[0], -x[1]))
        #print(res)
        return [e[1] for e in res[:k]]
