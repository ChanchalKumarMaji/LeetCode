def check(matrix):
    sr1=sum(matrix[0])
    sr2=sum(matrix[1])
    sr3=sum(matrix[2])
    
    sc1=matrix[0][0] + matrix[1][0] + matrix[2][0] 
    sc2=matrix[0][1] + matrix[1][1] + matrix[2][1]
    sc3=matrix[2][0] + matrix[2][1] + matrix[2][2]
    
    sd1=matrix[0][0] + matrix[1][1] + matrix[2][2]
    sd2=matrix[2][0] + matrix[1][1] + matrix[0][2]
    
    l=[]
    for i in range(3):
        for j in range(3):
            if matrix[i][j]>9 or matrix[i][j]<1:
                return False 
            l.append(matrix[i][j]) 
    
    if sr1==sr2==sr3==sc1==sc2==sc3==sd1==sd2 and len(set(l))==9:
        return True
    return False 

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0]) 
        
        count=0
        
        for i in range(r-2):
            for j in range(c-2):
                l=[]
                l.append(grid[i][j:j+3])
                l.append(grid[i+1][j:j+3])
                l.append(grid[i+2][j:j+3])
                #print(l)
                if check(l):
                    count+=1
        
        return count
