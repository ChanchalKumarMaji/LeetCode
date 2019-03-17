class Solution:
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pattern=list(pattern)
        s=s.split()
        if len(pattern)!=len(s):
            return False
        return len(set(zip(pattern,s)))==len(set(pattern))==len(set(s))
