class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        for n in range(left, right+1):
            t = str(n)
            flag = 1
            if "0" in t:
                continue
            for e in t:
                if n % (int(e)) != 0:
                    flag = 0
                    break
            if flag == 1:        
                l.append(n)
                
        return l
