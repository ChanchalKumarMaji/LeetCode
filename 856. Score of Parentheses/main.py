class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        l = list(S)
        print(l)
        s = []
        for i in range(len(S)):
            if S[i] == '(':
                s.append('(') 
            elif S[i] == ')':
                if s[-1] == '(':
                    s.pop()
                    s.append(1)
                else:
                    r = 0
                    while str(s[-1]).isdigit():
                        r += s[-1]
                        s.pop()
                    s.pop()
                    s.append(2*r)
        print(s)            
        return sum(s)
