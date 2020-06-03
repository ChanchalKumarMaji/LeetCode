class Solution:
    def isValid(self, x, y1, y2):
        return (x>=0 and x<self.R) and (y1>=0 and y1 < self.C) and (y2>=0 and y2 < self.C)
    
    def help(self, x, y1, y2):
        if not self.isValid(x, y1, y2):
            return -1000000
        if x==self.R-1:
            return self.grid[x][y1] if y1==y2 else (self.grid[x][y1] + self.grid[x][y2])
        if self.dp[x][y1][y2] != -1:
            return self.dp[x][y1][y2]
        ans = -1000000
        temp = self.grid[x][y1] if y1==y2 else (self.grid[x][y1] + self.grid[x][y2])
        
        ans = max(ans, temp + self.help(x+1, y1, y2-1))
        ans = max(ans, temp + self.help(x+1, y1, y2+1))
        ans = max(ans, temp + self.help(x+1, y1, y2))
        
        ans = max(ans, temp + self.help(x+1, y1-1, y2))
        ans = max(ans, temp + self.help(x+1, y1-1, y2-1))
        ans = max(ans, temp + self.help(x+1, y1-1, y2+1))
        
        ans = max(ans, temp + self.help(x+1, y1+1, y2))
        ans = max(ans, temp + self.help(x+1, y1+1, y2-1))
        ans = max(ans, temp + self.help(x+1, y1+1, y2+1))
        
        self.dp[x][y1][y2] = ans
        return self.dp[x][y1][y2]
        
    
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.R, self.C = len(grid), len(grid[0])
        self.grid = grid
        self.dp = [[[-1 for _ in range(self.C)] for j in range(self.C)] for i in range(self.R)]
        return self.help(0, 0, self.C-1)
