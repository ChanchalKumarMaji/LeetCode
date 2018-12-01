class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if len(s)==0:
            return 0
        return len((s.split(" "))[-1])
