class Solution(object):
    def minimumLengthEncoding(self, words):
        good = set(words)
        words=list(good)
        for word in words:
            for k in range(1, len(word)):
                if word[k:] in good:
                    good.remove(word[k:])

        return sum(len(word) + 1 for word in good)
