dr=[-1,1,0,0]
dc=[0,0,-1,1]
R=0
C=0
_grid=[]       
def floodfill( r, c, c1, c2):
    if r<0 or r>=R or c<0 or c>=C:
        return 0
    if _grid[r][c]!=c1:
        return 0
    ans=1
    _grid[r][c]=c2
    for d in range(4):
        ans+= floodfill(r+dr[d],c+dc[d],c1,c2)
    return ans

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        global R,C,_grid
        _grid=grid
        R=len(grid)
        if R==0:
            return 0
        C=len(grid[0])
        count=0
        for i in range(R):
            for j in range(C):
                if floodfill(i,j,'1','-1')>0:
                    count+=1
                    
        return count
