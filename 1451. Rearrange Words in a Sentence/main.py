class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.lower().split()
        res = []
        for i, word in enumerate(text):
            res.append((len(word), i, word))
        res.sort()
        p = " ".join([i[2] for i in res])
        return p[0].upper() + p[1:]
