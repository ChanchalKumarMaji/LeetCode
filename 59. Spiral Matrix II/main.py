class Solution:
    def generateMatrix(self, n):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix=[[0 for j in range(n)] for i in range(n)]
        
        i1=0
        i2=n-1
        j1=0
        j2=n-1
        
        k=1
        
        while i1<=i2 and j1<=j2:
            
            for i in range(j1,j2+1):
                matrix[i1][i]=k
                k+=1
            i1+=1
            
            for i in range(i1,i2+1):
                matrix[i][j2]=k
                k+=1
            j2-=1
            
            if i1<=i2:
                for i in range(j2,j1-1,-1):
                    matrix[i2][i]=k
                    k+=1
                i2-=1
            
            if j1<=j2:
                for i in range(i2,i1-1,-1):
                    matrix[i][j1]=k
                    k+=1
                j1+=1
        
        
                
        return matrix
