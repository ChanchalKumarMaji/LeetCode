class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        b_=[str(i) for i in b]
        
        B=int(''.join(b_)) 
        
        return pow(a,B,1337)
