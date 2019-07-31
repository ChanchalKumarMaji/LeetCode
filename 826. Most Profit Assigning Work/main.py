class Solution:
    def maxProfitAssignment(self, difficulty, profit, worker):
        """
        :type difficulty: List[int]
        :type profit: List[int]
        :type worker: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(difficulty)):
            l.append((difficulty[i],profit[i]))
        l.sort()    
            
        dif=[0 for i in range(100000+1)]
        
        m=l[0][1]
        for i in range(1,len(l)):
            
            for j in range(l[i-1][0],l[i][0]):
                dif[j]=m
            m=max(m,l[i][1])    
                
        s=0        
        for w in worker:
            if w>=l[-1][0]:
                s=s+m
            else:    
                s=s+dif[w]
            
        return s
