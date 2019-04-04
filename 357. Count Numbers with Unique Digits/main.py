class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        N=[1, 9]
        f = 9
        p = 9
        for i in range(2,10+1):
            f = f*p
            p -= 1
            N.append(f) 
            
        print(N)
        
        return sum(N[:n+1])
