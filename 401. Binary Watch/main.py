class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        hour = []
        for i in range(0, 12):
            bit = [0, 0, 0, 0]
            n = i
            for j in range(3, -1, -1):
                bit[j] = n%2
                n = n//2
            hour.append(bit) 
        #print(hour)    
        
        minute = []
        for i in range(0, 60):
            bit = [0, 0, 0, 0, 0, 0]
            n = i
            for j in range(5, -1, -1):
                bit[j] = n%2
                n = n//2
            minute.append(bit) 
        #print(minute)
        
        res = []
        for i in range(len(hour)):
            h = i
            b = num - hour[i].count(1) 
            if b>=0:
                for j in range(len(minute)):
                    if minute[j].count(1) == b:
                        m = j 
                        res.append('%d:%02d' %(h, m)) 
                        
        return res
