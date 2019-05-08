class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        row1="qwertyuiop"
        row2="asdfghjkl"
        row3="zxcvbnm"  
        
        res=[]
        
        for word in words:
            if set(word.lower()).issubset(set(row1)) or set(word.lower()).issubset(set(row2)) or set(word.lower()).issubset(set(row3)):
                res.append(word)
                 
                    
                    
        return res
