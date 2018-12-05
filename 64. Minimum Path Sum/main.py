class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])  
        
        matrix = [[0 for j in range(c)] for i in range(r)]
        
        matrix[0][0] = grid[0][0] 
        for j in range(1, c):
            matrix[0][j] = matrix[0][j-1] + grid[0][j]
        for i in range(1, r):
            matrix[i][0] = matrix[i-1][0] + grid[i][0] 
            
        for i in range(1, r):
            for j in range(1, c):
                matrix[i][j] = min(matrix[i-1][j], matrix[i][j-1]) + grid[i][j] 
                
        return matrix[-1][-1]
