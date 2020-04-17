class Solution:
    def entityParser(self, text: str) -> str:
        entity = ["&quot;", "&apos;", "&amp;", "&gt;", "&lt;", "&frasl;"]
        char = ['"', "'", "&", ">", "<", "/"]
        res = ""
        i = 0
        while i < len(text):
            f = False
            if text[i] == '&':
                for j in range(6):
                    e, c = entity[j], char[j]
                    if text[i: i+len(e)] == e:
                        res += c
                        i += len(e) - 1
                        f = True
                        break
            else:
                res += text[i]
            if text[i] == '&' and not f:
                res += '&'
            i += 1
        return res
