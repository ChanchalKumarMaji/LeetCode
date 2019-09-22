from collections import Counter 
class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        d1 = Counter(A)
        d2 = Counter(B)
        
        if not d1==d2:
            return False
        
        if A == B and any(x>=2 for x in list(d1.values())):
            return True 
        
        c = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                c += 1
        if c == 2:
            return True
        
        return False
