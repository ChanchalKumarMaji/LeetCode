class Solution:
    def dfs(self, u):
        self.visited[u] = 1
        for v in self.AdjList[u]:
            if self.visited[v] == 0:
                self.dfs(v)
    
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n-1:
            return -1
        self.AdjList = [[] for _ in range(n)]
        for connection in connections:
            u, v = connection
            self.AdjList[u].append(v)
            self.AdjList[v].append(u)
        self.visited = [0]*n
        res = 0
        for i in range(n):
            if self.visited[i] == 0:
                res += 1
                self.dfs(i)
        
        return res-1
