import collections
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        graph = collections.defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            
        count = [1] * N
        ans = [0] * N
        
        def dfs1(node = 0, parent = None):
            for neighbour in graph[node]:
                if neighbour != parent:
                    dfs1(neighbour, node)
                    count[node] += count[neighbour]
                    ans[node] += ans[neighbour] + count[neighbour]
                    
        def dfs2(node = 0, parent = None):
            for neighbour in graph[node]:
                if neighbour != parent:
                    ans[neighbour] = ans[node] + N - 2*count[neighbour]
                    dfs2(neighbour, node)
                    
                    
        dfs1()
        dfs2()
        
        return ans
