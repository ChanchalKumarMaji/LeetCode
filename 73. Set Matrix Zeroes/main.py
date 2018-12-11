class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        r=len(matrix)
        c=len(matrix[0])
        
        zero_row=[0 for i in range(r)]
        zero_col=[0 for i in range(c)] 
        
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    zero_row[i]=1
                    zero_col[j]=1 
        
        #grid=[[0 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            if zero_row[i]==1:
                for j in range(c):
                    matrix[i][j]=0
                    
        for j in range(c):
            if zero_col[j]==1:
                for i in range(r):
                    matrix[i][j]=0
