class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        ll=[0 for i in range(len(S))]
        lr=[0 for i in range(len(S))]
        l=[0 for i in range(len(S))]
        count=[0 for i in range(len(S))]
        
        for i in range(len(S)):
            if S[i]==C:
                count[i]=0
            else:
                count[i]=1
        #return count        
                
        k=0        
        f=0
        for i in range(len(count)):
            if count[i]==0:
                k=0
                f=1
            elif f==1:
                k+=1
                ll[i]=k
        #return ll
        
        k=0        
        f=0
        p=count[::-1]
        for i in range(len(count)):
            if p[i]==0:
                k=0
                f=1
            elif f==1:
                k+=1
                lr[i]=k        
                
        
        lr=lr[::-1]
        #return lr
    
        for i in range(len(ll)):
            
            if ll[i]==0 or lr[i]==0:
                l[i]=max(ll[i],lr[i])
                
            else:
                l[i]=min(ll[i],lr[i])
                
        return l
