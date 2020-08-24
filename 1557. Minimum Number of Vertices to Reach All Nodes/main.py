class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        d = set([i for i in range(n)])
        for [u, v] in edges:
            if v in d:
                d.remove(v)
        return list(d)
