class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        AdjList = [set() for _ in range(n)]
        for (u, v) in edges:
            AdjList[u].add(v)
            AdjList[v].add(u)
        dfs_num = [0] * n
        count = [int(i) for i in hasApple]
        res = 0
        def dfs(u):
            dfs_num[u] = 1
            for v in AdjList[u]:
                if dfs_num[v] == 0:
                    count[u] += dfs(v)
            return count[u]
        _ = dfs(0)
        res = 0
        for e in count:
            if e > 0:
                res += 1
        return max(0, 2 * (res - 1))
