class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        elif n == 3:
            return 2
        elif n%3 == 0:
            return pow(3,n//3)
        elif n%3 == 1:
            return pow(3,n//3 -1)*4
        elif n%3 == 2:
            return pow(3,n//3)*2
