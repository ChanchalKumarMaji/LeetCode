class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        
        s="1"
        for i in range(n-1):
            
            t=s[0]
            s=s+"#"
            st=""
            for j in range(1,len(s)):
                
                if t[-1]==s[j]:
                    t=t+s[j]
                    
                else:
                    st=st+str(len(t))+t[0]
                    t=s[j]
            s=st        
            
            
        return s
