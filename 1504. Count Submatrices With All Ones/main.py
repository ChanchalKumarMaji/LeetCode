class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        prefix = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n-1, -1, -1):
                if mat[i][j] == 0:
                    continue
                if j != n-1:
                    prefix[i][j] += prefix[i][j+1]
                prefix[i][j] += mat[i][j]
        res = 0
        for j in range(n):
            i = m - 1
            q = []
            s = 0
            while i >= 0:
                c = 0
                while q and q[-1][0] > prefix[i][j]:
                    s -= (q[-1][1] + 1) * (q[-1][0] - prefix[i][j])
                    c += q[-1][1] + 1
                    _ = q.pop()
                s += prefix[i][j]
                res += s
                q.append((prefix[i][j], c))
                i -= 1
        return res
