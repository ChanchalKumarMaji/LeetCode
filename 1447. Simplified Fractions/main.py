from math import gcd
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = set()
        for i in range(1, n):
            for j in range(i+1, n+1):
                g = gcd(i, j)
                res.add(str(i//g)+"/"+str(j//g))
        return list(res)
