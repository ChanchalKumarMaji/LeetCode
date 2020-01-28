from collections import defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = defaultdict(list)
        m, n = len(mat), len(mat[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                d[i-j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                res[i][j] = d[i-j].pop()
        return res
