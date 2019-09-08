class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        n = len(S)
        l = [0]*n
        l[n-1] = shifts[n-1] 
        for i in range(n-2, -1, -1):
            l[i] = l[i+1] + shifts[i]
            
        #print(l)
        
        res = []
        for i in range(n):
            c = S[i]
            r = chr( (ord(c)-97 + l[i])%26 + 97 )
            res.append(r)
        print(res)    
        return ''.join(res)
