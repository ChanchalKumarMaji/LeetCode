class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        self.x=x
        f=0
        if x<0:
            f=1
        x=abs(x)
        x=str(x)
        k=len(x)
        s=""
        for i in range(k):
            s=x[i]+s
        s=int(s)
        if f==1:
            if s>2147483648:
                return 0
            return -1*s
        else:
            if s>2147483647:
                return 0
            return s
