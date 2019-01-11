class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        n=rowIndex
        l=[1]
        if n==0:
            return l
        
        num=1
        den=1
        for i in range(n//2):
            num=num*(n-i)
            den=den*(i+1)
            l.append(num//den)
        if n%2==1:
            l=l+l[::-1]
        else:
            l=l+l[-2::-1]
            
        return l
