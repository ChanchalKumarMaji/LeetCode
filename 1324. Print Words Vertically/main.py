class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = len(s)
        m = max([len(w) for w in s])
        res = [[" "]*n for _ in range(m)]
        for j in range(n):
            w = s[j]
            for i in range(len(w)):
                res[i][j] = w[i]
        ans = ["".join(e).rstrip() for e in res]
        return ans
