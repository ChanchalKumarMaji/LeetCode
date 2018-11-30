class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        length=len(matrix)
        
        if length==0:
            return []
        
        length1=len(matrix[0])
        
        i1=0
        i2=length-1
        j1=0
        j2=length1-1
        
        l=[]
        while i1<=i2 and j1<=j2:
            
            for i in range(j1,j2+1):
                l.append(matrix[i1][i])
            i1+=1
            
            for i in range(i1,i2+1):
                l.append(matrix[i][j2])
            j2-=1
            
            if i1<=i2:
                for i in range(j2,j1-1,-1):
                    l.append(matrix[i2][i])
                i2-=1
            
            if j1<=j2:
                for i in range(i2,i1-1,-1):
                    l.append(matrix[i][j1])
                j1+=1
        
        
                
        return l
