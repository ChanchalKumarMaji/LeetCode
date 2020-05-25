class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence = sentence.split()
        k = len(searchWord)
        for i, word in enumerate(sentence):
            if word[:k] == searchWord:
                return i+1
        return -1
