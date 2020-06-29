class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = []
        for i in range(1, n+1):
            if n % i == 0:
                res.append(i)
        res = list(set(res))
        res.sort()
        if k <= len(res):
            return res[k-1]
        return -1
