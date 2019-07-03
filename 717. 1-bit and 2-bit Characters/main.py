class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        while i<len(bits):
            if bits[i] == 0 and i == len(bits)-1:
                return True 
            if bits[i] == 1:
                i += 2
            elif bits[i] == 0:
                i += 1
                
        return False
