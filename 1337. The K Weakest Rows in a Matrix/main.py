class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        m, n = len(mat), len(mat[0])
        for i in range(m):
            res.append((mat[i].count(1), i))
        res.sort()
        return [e[1] for e in res[:k]]
