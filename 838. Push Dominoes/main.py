class Solution:
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        N=len(dominoes)
        
        forceR=[0 for i in range(N)]
        f=0
        for i in range(N):
            if dominoes[i]=='R': f=N
            elif dominoes[i]=='L': f=0
            else: f-=1    
            forceR[i] = max(f,0)
            
        #print(forceR)    
        
        forceL=[0 for i in range(N)]
        f=0
        for i in range(N-1,-1,-1):
            if dominoes[i]=='R': f=0
            elif dominoes[i]=='L': f=N
            else: f-=1    
            forceL[i] = -1*max(f,0)
            
        #print(forceL)   
        
        force = [0 for i in range(N)]
        for i in range(N):
            force[i] = forceR[i] + forceL[i] 
        #print(force)    
        
        res=[0 for i in range(N)]
        for i in range(N):
            if force[i]<0: res[i] = 'L'
            elif force[i]==0: res[i] = '.'
            elif force[i]>0: res[i] = 'R'
                
        #print(res) 
        
        return ''.join(res)
