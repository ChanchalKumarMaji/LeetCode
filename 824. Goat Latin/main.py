class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        l=S.split()
        fi=[]
        c=1
        for w in l:
            st=""
            if w[0]=='a' or w[0]=='e' or w[0]=='i' or w[0]=='o' or w[0]=='u' or w[0]=='A' or w[0]=='E' or w[0]=='I' or w[0]=='O' or w[0]=='U':
                st=w+"ma"
            else:
                st=w[1:]+w[0]+"ma"
            for i in range(c):
                st=st+"a"
            c+=1
            fi.append(st)
            
        return " ".join(fi)
