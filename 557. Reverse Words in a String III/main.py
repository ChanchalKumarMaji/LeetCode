class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words=[]
        for word in s.split(" "):
            words.append(word[::-1]) 
        return " ".join(words)
