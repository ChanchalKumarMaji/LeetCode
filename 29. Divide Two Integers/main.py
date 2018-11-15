class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1
        #print(sign)
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        
        while dividend>=divisor:
            d = divisor
            q = 1
            while dividend>=d:
                d = d<<1
                q = q<<1
            
            d = d>>1
            q = q>>1
            
            dividend = dividend - d
            res = res + q
            
        res =  -res if sign==-1 else res
        
        l = -2**31 
        r = 2**31 - 1
        
        if l <= res <= r:
            return res
        else:
            return r
