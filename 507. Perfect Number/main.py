class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<2:
            return False
        s=1
        for i in range(2,int(math.sqrt(num))+1): 
            if num%i==0:
                s=s+(i)+(num//i)
            
        return s==num
