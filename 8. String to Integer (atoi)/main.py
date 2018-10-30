class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        count=0
        sign=1
        st='0'
        s=s.strip()
        for i in range(len(s)):
                
            if ord(s[i])>=48 and ord(s[i])<=57:
                st=st+s[i]
            
            elif s[i]=='+' and count==0:
                count=1
            elif s[i]=='+' and count==1:
                break
                
            elif s[i]=='-' and count==0:
                sign=-1
                count=1
            elif s[i]=='-' and count==1:
                break    
    
            else:
                break
                
        n=sign*(int(st))        
        
        if n>=2147483647:
            return 2147483647
        elif n<=-2147483648:
            return -2147483648
        else:
            return n
