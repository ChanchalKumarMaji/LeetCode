class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.N=N
        count=0
        
        for i in range(1,N+1):
            f=1
            s=str(i)
            arr=[0 for i in range(10)]
            for c in s:
                arr[int(c)]+=1    
            
            if arr[4]!=0 or arr[7]!=0 or arr[3]!=0 :
                continue
            if arr[2]!=0 or arr[5]!=0 or arr[6]!=0 or arr[9]!=0 :
                count+=1
                print(i)
                
        return count
