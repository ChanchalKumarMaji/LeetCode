class Solution:
    def dfs(self, u):
        self.dfs_num[u] = 1
        for v in self.AdjList[u]:
            if self.dfs_num[v] == 0:
                self.value[u] += self.dfs(v)
        return self.value[u]
    
    def _dfs(self, u):
        if self.value[u] == 0:
            return
        self.res += 1
        self.dfs_num[u] = 1
        for v in self.AdjList[u]:
            if self.dfs_num[v] == 0:
                self._dfs(v)
    
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        self.res = 0
        n = nodes
        self.dfs_num = [0]*n
        self.AdjList = [[] for _ in range(n)]
        self.value = value
        for v in range(1, n):
            u = parent[v]
            self.AdjList[u].append(v)
        k = self.dfs(0)
        print(self.value)
        self.dfs_num = [0]*n
        self._dfs(0)
        
        return self.res
