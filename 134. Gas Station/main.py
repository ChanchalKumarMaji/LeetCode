class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        
        start, g, Min = 0, 0, sys.maxsize 
        
        for i in range(len(gas)):
            g += gas[i] - cost[i]
            if g<Min:
                start = (i+1)%len(gas)
                Min = g
        return start
