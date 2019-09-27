class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        r = len(A)
        c = len(A[0])
        
        for i in range(r):
            if A[i][0] == 0:
                for j in range(c): 
                    A[i][j] = 1 - A[i][j]
                    
        for j in range(1, c):
            count_1 = 0
            for i in range(r):
                if A[i][j] == 1:
                    count_1 += 1
            maj = (r//2) if r%2==0 else (r//2 + 1)
            if count_1 < maj:
                for i in range(r):
                    A[i][j] = 1 - A[i][j] 
        
        res = 0
        for i in range(r):
            l = A[i]
            l = [str(e) for e in l]
            res += int(''.join(l), 2)
            
        return res
