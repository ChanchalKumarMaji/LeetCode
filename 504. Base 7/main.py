class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        l=[]
        if num==0:
            return "0"
        if num<0:
            f=-1
        else:
            f=1
        num=abs(num)    
        while num!=0:
            l.append(str(num%7))
            num=num//7
        #print(l)    
        
        s=''.join(l[::-1])
        if f==-1:
            return "-"+s
        return s
