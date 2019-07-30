class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        l=[0 for i in range(120+1)] 
        for age in ages:
            l[age]+=1
            
        count=0
        
        for i in range(120,0,-1):
            if l[i]!=0:
                
                if not((i>100 and i<100) or (i<=(0.5*i)+7)):
                    count+=l[i]*(l[i]-1)
                
                for j in range(i-1,-1,-1):
                    if (l[j]==0) or (j>100 and i<100) or (j<=(0.5*i)+7): 
                        continue
                    else:
                        count+=l[i]*l[j] 
                
        
            
        return count
