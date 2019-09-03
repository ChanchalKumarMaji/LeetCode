class Solution:
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l = [0 for i in range(len(A))]
        A = A + [-1]
        count = 0
        for i in range(1, len(A)):
            if A[i-1] < A[i]:
                count += 1
            else:
                l[i-1] = count + 1
                count = 0
                
        A = A[:-1]
        #print(A)
        #print(l)
        
        k = A[::-1] + [-1]
        #print(k)
        r = [0 for i in range(len(A))]
        count = 0
        for i in range(1, len(k)):
            if k[i-1] < k[i]:
                count += 1
            else:
                r[i-1] = count + 1
                count = 0
        r = r[::-1]        
        #print(r)   
        
        m = 0
        
        for i in range(len(A)):
            if l[i]>1 and r[i]>1:
                if l[i]+r[i]-1 >= 3:
                    m = max(m, l[i]+r[i]-1)
                
        return m
