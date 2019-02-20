class Solution:

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s=s
        if s=="":
            return ""
        size=len(s)
        rev=s[::-1]
        for i in range(size):
            if s[0:size-i]==rev[i:]:
                return rev[0:i]+s
