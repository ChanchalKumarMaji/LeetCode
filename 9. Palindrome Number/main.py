class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        self.x=x
        if x<0:
            return False
        x=str(x)
        length=len(x)
        i=0
        j=length-1
        
        for i in range(length//2):
            if x[i]!=x[length-i-1]:
                return False
                
        return True
