class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        self.s=s
        no_of=0
        length=len(s)
        table=[[0 for j in range(length)] for i in range(length)]

        for i in range(length):
            table[i][i]=1
            no_of+=1 
    
        for i in range(length-1):
            if s[i]==s[i+1]:
                table[i][i+1]=1
                no_of+=1 
        
        count=2
        for k in range(length-2,0,-1):
            for i in range(k):        
                j=i+count
                if table[i+1][j-1] and s[i]==s[j]:
                    table[i][j]=1
                    no_of+=1
            count=count+1    
                

        return no_of
