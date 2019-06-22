class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        s=[]
        for op in ops:
            if op=="+":
                s.append(s[-1]+s[-2])
            elif op=="D":
                s.append(2*s[-1])
            elif op=="C":
                s.pop()
            else:
                s.append(int(op)) 
                
        #print(s)
        return sum(s)
