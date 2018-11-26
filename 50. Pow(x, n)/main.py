class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def power(x, y):
            res = 1
            while y>0:
                if y%2==1:
                    res = res*x
                y = y//2
                x = x*x
            return res
        
        if n<0:
            return 1/power(x, -n)
        return power(x, n)
