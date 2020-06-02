class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        AdjMat = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            AdjMat[i][i] = 1;
        for (u, v) in prerequisites:
            AdjMat[u][v] = 1
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    AdjMat[i][j] = AdjMat[i][j] | (AdjMat[i][k] & AdjMat[k][j])
        res = []
        for (u, v) in queries:
            if AdjMat[u][v] == 1:
                res.append(True)
            else:
                res.append(False)
        return res
