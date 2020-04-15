class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        k = 0
        s = 0
        A.append(0.1)
        for i in range(2, len(A)):
            if A[i-2]-A[i-1] == A[i-1]-A[i]:
                k += 1
            else:
                s = s+(k)*(k+1)//2
                k = 0
                
        return s
