class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        if m==0:
            return False
        n = len(matrix[0])
        
        r = 0
        c = n-1
        
        while r<m and c>=0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:    
                c -= 1
                
        return False
