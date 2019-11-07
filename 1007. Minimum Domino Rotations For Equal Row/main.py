class Solution:
    def max_item(self, A):
        a = [0]*7
        for e in A:
            a[e] += 1
        a_max = []
        m = max(a)
        for i in range(1, len(a)):
            if a[i] == m:
                a_max.append(i)
        return a_max
    
    def num_rot(self, e, A, B):
        res = 0
        for i in range(len(A)):
            if A[i] != e:
                if B[i] == e:
                    res += 1
                else:
                    return -1
        return res
    
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:        
        max_a = self.max_item(A)
        max_b = self.max_item(B)
        #print(max_a, max_b)
        res = []
        
        for e in max_a:
            r = self.num_rot(e, A, B)
            #print(e, r)
            if r != -1:
                res.append(r)
        
        for e in max_b:
            r = self.num_rot(e, B, A)
            #print(e, r)
            if r != -1:
                res.append(r)
        
        if res == []:
            return -1
        return min(res)
