class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        for a in A:
            res.append(a[::-1])
         
        for i in range(len(A)):
            for j in range(len(A[0])):
                if res[i][j]==1:
                    res[i][j]=0
                else:
                    res[i][j]=1
            
        return res
