class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l1=len(a)
        l2=len(b)
        
        if l1>l2:
            for i in range(l1-l2):
                b='0'+b
        if l1<l2:
            for i in range(l2-l1):
                a='0'+a
        
        s=''
        c=0
        for i in range(len(a)-1,-1,-1):
            da=int(a[i])
            db=int(b[i])
            d=da+db+c
            if d==0:
                s='0'+s
                c=0
            elif d==1:
                s='1'+s
                c=0
            elif d==2:
                s='0'+s
                c=1
            elif d==3:
                s='1'+s
                c=1
         
        if c==1:
            s='1'+s
            
        return s
