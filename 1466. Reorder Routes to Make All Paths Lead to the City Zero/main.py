class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        AdjList = [set() for _ in range(n)]
        p = set()
        for (u, v) in connections:
            AdjList[u].add(v)
            AdjList[v].add(u)
            p.add((u, v))
        d = [-1] * n
        d[0] = 0
        q = collections.deque([0])
        res = set()
        while q:
            u = q.popleft()
            for v in AdjList[u]:
                if d[v] == -1:
                    res.add((u, v))
                    d[v] = d[u] + 1
                    q.append(v)
        return len(p.intersection(res))
