class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        i = 0
        c1 = 0
        while seats[i] != 1:
            c1 += 1
            i += 1
            
        c2 = 0
        j = n-1
        while seats[j] != 1:
            c2 += 1
            j -= 1
            
        #print(c1)
        #print(c2)
        seats = seats[i:j+1]
        
        c = 0
        n = len(seats)
        res = 0
        for i in range(1,n):
            if seats[i] == 1:
                #print(c)
                print((c-1)//2 +1)
                res = max((c-1)//2 + 1, res)
                c = 0
            else:
                c += 1
        return max(res, c1, c2)
