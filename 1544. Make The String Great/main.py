class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for e in s:
            stack.append(e)
            if len(stack) >= 2 and abs(ord(stack[-1]) - ord(stack[-2])) == 32:
                _ = stack.pop()
                _ = stack.pop()
        return ''.join(stack)
