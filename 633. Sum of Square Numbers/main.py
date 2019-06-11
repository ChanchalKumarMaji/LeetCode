import math

def isSquare(k):
    p=math.sqrt(k)
    return int(p)==p 
    
class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        if isSquare(c):
            return True 
        
        for i in range(int(math.sqrt(c//2)),int(math.sqrt(c))+1): 
            k=c-i*i
            if isSquare(k): 
                return True
        return False
