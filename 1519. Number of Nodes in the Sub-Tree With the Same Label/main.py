class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        AdjList = [set() for _ in range(n)]
        for (u, v) in edges:
            AdjList[u].add(v)
            AdjList[v].add(u)
        dfs_num = [0] * n
        res = [[0]*26 for _ in range(n)]
        ans = [0] * n
        
        def i(c):
            return ord(c) - 97
        
        def dfs(u):
            dfs_num[u] = 1
            res[u][i(labels[u])] += 1
            ans[u] += 1
            for v in AdjList[u]:
                if dfs_num[v] == 0:
                    d = dfs(v)
                    for t in range(26):
                        res[u][t] += d[t]
                    ans[u] += d[i(labels[u])]
            return res[u]
        dfs(0)
        return ans
