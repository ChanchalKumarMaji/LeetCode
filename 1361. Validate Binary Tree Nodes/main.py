class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        AdjList = [[] for _ in range(n)]
        edges = 0
        for i in range(n):
            AdjList[i] = (leftChild[i], rightChild[i])
            if leftChild[i] != -1:
                edges += 1
            if rightChild[i] != -1:
                edges += 1
            if (0 <= leftChild[i] < i) or (0 <= rightChild[i] < i):
                return False
        #print(AdjList)
        visited = [-1]*n
        def dfs(u):
            if u == -1:
                return
            visited[u] = 0
            for v in AdjList[u]:
                if visited[v] == -1:
                    dfs(v)
        dfs(0)
        #print(visited, edges)
        if edges == n-1 and sum(visited) == 0:
            return True
        
        return False
