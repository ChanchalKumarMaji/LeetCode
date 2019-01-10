class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        l=[]
        if numRows==0:
            return l
        l.append([1])
        if numRows==1:
            return l
        l.append([1,1])
        if numRows==2:
            return l
        for i in range(1,numRows-1):
            p=[]
            p.append(1)
            for j in range(1,len(l[i])):
                p.append(l[i][j]+l[i][j-1])
            p.append(1)
            l.append(p)
            
        return l
