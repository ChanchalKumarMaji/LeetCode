class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        h = mat[0][:]
        for row in mat[1:]:
            h = sorted([i+j for i in row for j in h])[:k]
        return h[k-1]
