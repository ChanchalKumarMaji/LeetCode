class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls=len(s)
        lp=len(p)
        
        res = []
        
        if ls<lp:
            return res
        
        check = [0 for i in range(26)]
        for e in p:
            check[ord(e)-97] += 1
        
        window = [0 for i in range(26)]
        for e in s[0:0+lp]:
            window[ord(e)-97] += 1
            
        if window == check:
            res.append(0)
            
        for i in range(1,ls-lp+1):    
            window[ord(s[i-1])-97] -= 1
            window[ord(s[i-1+lp])-97] += 1
            
            if window == check:
                res.append(i)
                
        return res
