class Solution:
    def lenLongestFibSubseq(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        d = set(A)
        res = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                a, b = A[i], A[j]
                count = 2
                while a+b in d:
                    count += 1
                    c = a+b
                    a = b
                    b = c
                res = max(res, count) 
        
        if res>=3:
            return res 
        return 0
