class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = [0]
        for i in range(1, n+1):
            l1 = l
            l2 = l[::-1]
            k = 2**(i-1)
            for j in range(len(l2)):
                l2[j] += k 
            l = l1 + l2
            
        return l
