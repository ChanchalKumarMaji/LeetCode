class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        INF = float("inf")
        AdjMat = [[INF]*n for _ in range(n)]
        for i in range(n):
            AdjMat[i][i] = 0
        for edge in edges:
            u, v, w = edge
            AdjMat[u][v] = w
            AdjMat[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    AdjMat[i][j] = min(AdjMat[i][j], AdjMat[i][k] + AdjMat[k][j])
        #print(AdjMat)
        d = {}
        for i in range(n):
            c = -1
            for j in range(n):
                if AdjMat[i][j] <= distanceThreshold:
                    c += 1
            d[i] = c
        #print(d)
        m = min(d.values())
        res = 0
        for k in d:
            if d[k] == m:
                res = max(res, k)
        return res
