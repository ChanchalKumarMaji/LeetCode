class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        take=[]
        delete=[]
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                delete.append(fronts[i])
        #delete=set(delete)
        
        for i in range(len(fronts)):
            if fronts[i] not in delete:
                take.append(fronts[i])
            if backs[i] not in delete:
                take.append(backs[i])
                    
        
        if len(take)==0:
            return 0
        else:
            take.sort()
            return take[0]
