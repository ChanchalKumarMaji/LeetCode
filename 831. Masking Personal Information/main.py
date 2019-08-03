def hasNumbers(s):
    return any(char.isdigit() for char in s)

class Solution:
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if any(char.isdigit() for char in S):
            l=[]
            for i in S:
                if i.isdigit():
                    l.append(i)
            
            l=l[::-1]
            t=l[0]+l[1]+l[2]+l[3]+"-"+"***"+"-"+"***"
            if len(l)>10:
                t+="-"
                for i in range(10,len(l)):
                    t+="*"
                t+="+"
                
            return t[::-1] 
        
        else:
            n1=(S[:S.find("@")]).lower()
            n2=(S[S.find("@")+1:S.find(".")]).lower()
            n3=(S[S.find(".")+1:]).lower()
            
            t=n1[0]+"*****"+n1[-1]+"@"+n2+"."+n3
            
            return t
