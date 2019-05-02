class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r=len(grid)
        c=len(grid[0])
        
        #matrix=[[0 for j in range(c)] for i in range(r)]
        res=0 
        for i in range(r):
            for j in range(c):
                count=0
                if grid[i][j]==1:
                    if (i-1==-1) or (grid[i-1][j]==0):
                        count+=1
                    if (i+1==r) or (grid[i+1][j]==0):
                        count+=1
                    if (j-1==-1) or (grid[i][j-1]==0):
                        count+=1
                    if (j+1==c) or (grid[i][j+1]==0):
                        count+=1    
                
                res+=count
                
        return res
