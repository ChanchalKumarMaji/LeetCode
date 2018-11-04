class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        d['I'] = 1
        d['IV'] = 4
        d['V'] = 5
        d['IX'] = 9
        d['X'] = 10
        d['XL'] = 40
        d['L'] = 50
        d['XC'] = 90
        d['C'] = 100
        d['CD'] = 400
        d['D'] = 500
        d['CM'] = 900 
        d['M'] = 1000  
        
        res = []
        for i in range(len(s)):
            res.append(d[s[i]])
        
        for i in range(len(res)-2, -1, -1):
            if res[i] < res[i+1]:
                res[i] *= -1
            
        #print(res) 
                
        return sum(res)
