class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for token in tokens:
            if token == "+":
                r=stack.pop()
                l=stack.pop()
                stack.append(l+r)
            elif token == "-":
                r=stack.pop()
                l=stack.pop()
                stack.append(l-r)
            elif token == "*":
                r=stack.pop()
                l=stack.pop()
                stack.append(l*r)
            elif token == "/":
                r=stack.pop()
                l=stack.pop()
                stack.append(int(l/r))
            else:
                stack.append(int(token))
            #print(stack)    
        return stack[0]
