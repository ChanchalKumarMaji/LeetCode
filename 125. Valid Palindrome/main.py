class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=''
        for i in range(len(s)):
            k=ord(s[i])
            if (k>=48 and k<=57) or (k>=97 and k<=122):
                st=st+s[i]
            if (k>=65 and k<=90):
                st=st+chr(k+32)
                
        return st==st[::-1]
