class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        d = {}
        d[1] = 'I'
        d[4] = 'IV'
        d[5] = 'V'
        d[9] = 'IX'
        d[10] = 'X'
        d[40] = 'XL'
        d[50] = 'L'
        d[90] = 'XC'
        d[100] = 'C'
        d[400] = 'CD'
        d[500] = 'D'
        d[900] = 'CM' 
        d[1000] = 'M' 
        
        m = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        res = ""
        for i in range(len(m)):
            k = num//m[i] 
            num = num%m[i] 
            for j in range(k):
                res += d[m[i]]
                
        return res
