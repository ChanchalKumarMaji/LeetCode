class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        l = [str(2**i) for i in range(32)] 
        #print(l) 
        s = str(N)
        s = list(s)
        s.sort() 
        for i in range(32):
            t = list(l[i])
            t.sort()
            if s==t:
                return True
            
        return False
