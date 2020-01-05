class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for e in s:
            stack.append(e)
            if stack[-1]=='#':
                _ = stack.pop()
                b = stack.pop()
                a = stack.pop()
                stack.append(chr(int(a+b)+96))
        for i in range(len(stack)):
            if stack[i].isdigit():
                stack[i] = chr(int(stack[i])+96)
        return ''.join(stack)
