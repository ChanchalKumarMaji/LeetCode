class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        row, col = [0]*n, [0]*m
        for index in indices:
            r, c = index
            row[r] = 1 - row[r]
            col[c] = 1 - col[c]
        count = 0
        for i in range(n):
            for j in range(m):
                count += (row[i] + col[j]) % 2
                
        return count
