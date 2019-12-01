class Solution:
    def toHexspeak(self, num: str) -> str:
        h = hex(int(num))[2:]
        print(h)
        res = ""
        for e in h:
            if e == '0':
                res += 'O'
            elif e == '1':
                res += 'I'
            elif e in ['a', 'b', 'c', 'd', 'e', 'f']:
                res += e.upper()
            else:
                return "ERROR"
         
        return res
