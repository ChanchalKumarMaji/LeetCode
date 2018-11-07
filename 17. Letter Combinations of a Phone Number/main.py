class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        def help(l1, l2):
            l = []
            for i in range(len(l1)):
                for j in range(len(l2)):
                    l.append(l1[i]+l2[j]) 
            return l
        
        d = {}
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']
        
        l = []
        for digit in digits:
            l.append(d[digit]) 
        print(l) 
        
        while len(l)>1:
            l = [help(l[0], l[1])] + l[2:]
            
        #print(l)
        return l[0]
