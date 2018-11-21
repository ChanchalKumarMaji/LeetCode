class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2) 
        
        res = [0 for i in range(l1+l2)] 
        for j in range(l2-1, -1, -1):
            for i in range(l1-1, -1, -1):
                d = int(num2[j]) * int(num1[i]) + res[i+j+1]
                res[i+j] += d//10 
                res[i+j+1] = d%10
                
        i = 0
        while i<len(res)-1 and res[i]==0:
            i += 1
        t = ''
        for e in res[i:]:
            t += str(e)
        return t
