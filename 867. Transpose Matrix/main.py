class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        r = len(A)
        c = len(A[0])
        r, c = c, r
        res = [[0 for j in range(c)] for i in range(r)]
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                res[j][i] = A[i][j] 
                
        return res
