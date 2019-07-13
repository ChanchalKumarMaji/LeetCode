class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        c=0
        for s in S:
            if s.isalpha():
                c+=1      
        res=[]        
        for i in range(2**c):
            l=[]
            for t in S[::-1]:
                if t.isdigit():
                    l.append(t)
                elif t.isalpha():
                    if i%2==1:
                        l.append(t.upper())
                        i=i//2
                    else:
                        l.append(t.lower())
                        i=i//2
                        
            l=l[::-1]
            res.append(''.join(l))
            
        return res
