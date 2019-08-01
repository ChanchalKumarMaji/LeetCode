import math
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        n=N
        l=[]
        c=0
        while n%2==0:
            n=n//2
            c+=1
        if n==1:
            return 1
        res=1
        for i in range(3,int(math.sqrt(n))+1,2):
            c=0
            while n%i==0:
                c+=1
                #print(i)
                n=n//i
            res=res*(c+1)     
            
        if n>2:
            return res*2
        else:
            return res
