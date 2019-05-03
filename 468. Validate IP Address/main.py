class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP:
            l=IP.split(".")
            if len(l)!=4:
                return "Neither"
            else:
                digits=['0','1','2','3','4','5','6','7','8','9']
                for e in l:
                    if (len(e)>1 and e[0]=='0') or len(e)==0:
                        return "Neither"
                    else:
                        for c in e:
                            if c not in digits:
                                return "Neither"
                        if int(e)<0 or int(e)>255:
                            return "Neither"
                                
                        
            return "IPv4"        
            
            
        if ':' in IP:
            l=IP.split(":")
            if len(l)!=8:
                return "Neither"
            else:
                digits=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','a','b','c','d','e','f']
                for e in l:
                    if len(e)==0 or len(e)>4:
                        return "Neither"
                    else:
                        for c in e:
                            if c not in digits:
                                return "Neither"
            return "IPv6"                
            
            
        
        return "Neither"
