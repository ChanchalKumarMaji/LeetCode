class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s
        rows = 2*numRows - 2
        s = list(s)
        grid = []
        for i in range(0, len(s), rows):
            grid.append(s[i:i+rows])
        l = grid[-1]
        for i in range(rows - len(l)):
            grid[-1].append('') 
        #print(grid)     
        
        res = ""
        r = len(grid)
        c = len(grid[0])
        for i in range(r):
            res += grid[i][0]
        I, J = 1, c-1    
        for k in range((c+1)//2):
            for i in range(r):
                if I != J:
                    res += grid[i][I] + grid[i][J]
                else:
                    res += grid[i][I]
            I += 1
            J -= 1
            
        return res
