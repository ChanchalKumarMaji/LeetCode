class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        check=[0 for i in range(26)]
        
        for c in magazine:
            check[ord(c)-97]+=1
        for c in ransomNote:
            check[ord(c)-97]-=1
            
        for i in check:
            if i<0:
                return False
        
        return True
