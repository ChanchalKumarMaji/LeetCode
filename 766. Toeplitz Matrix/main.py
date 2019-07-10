class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        r=len(matrix)
        c=len(matrix[0])
        
        for k in range(c):
            j=k
            i=0
            while i+1<r and j+1<c:
                if matrix[i+1][j+1]!=matrix[i][j]:
                    return False
                i+=1
                j+=1
                
        for k in range(1,r):
            j=0
            i=k
            while i+1<r and j+1<c:
                if matrix[i+1][j+1]!=matrix[i][j]:
                    return False        
                i+=1
                j+=1
                
        return True
