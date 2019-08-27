def solve(s):
    st = []
    for e in s:
        if e == '#':
            if len(st) != 0:
                st.pop()
        else:
            st.append(e) 
            
    return "".join(st)         
                

class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        return (solve(S)) == (solve(T))
