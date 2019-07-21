class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        
        matrix=[[101 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            m=max(grid[i]) 
            for j in range(c):
                matrix[i][j]=min(m,matrix[i][j])
                
        for j in range(c):
            m=0
            for i in range(r):
                m=max(m,grid[i][j])
            for i in range(r):
                matrix[i][j]=min(m,matrix[i][j])
           
        s=0
        for i in range(r): 
            for j in range(c):
                s+=abs(matrix[i][j]-grid[i][j])   
                
        return s
