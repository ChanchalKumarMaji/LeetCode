class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1=len(s1)
        l2=len(s2)
        
        if l1>l2:
            return False
        
        check = [0 for i in range(26)]
        for e in s1:
            check[ord(e)-97] += 1
            
        #print(check)    
        
        window = [0 for i in range(26)]
        for e in s2[0:0+l1]:
            window[ord(e)-97] += 1
        
        if window==check:
            return True
        
        for i in range(1,l2-l1+1):
            #print(s2[i:i+l1])
            
            window[ord(s2[i+l1-1])-97] += 1
            window[ord(s2[i-1])-97] -=1
            
            #print(l)
            if window==check:
                return True 
          
        return False
