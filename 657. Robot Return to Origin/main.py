class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        l=[0,0,0,0]
        
        for c in moves:
            if c=='L':
                l[0]+=1
            elif c=='R':
                l[1]+=1
            elif c=='U':
                l[2]+=1
            else:
                l[3]+=1
        return l[0]==l[1] and l[2]==l[3]
