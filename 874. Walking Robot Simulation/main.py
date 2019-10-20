class Solution:
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1] 
        d = set(map(tuple, obstacles)) 
        x, y, di = 0, 0, 1
        res = 0
        for command in commands: 
            if command == -1:
                di = (di-1)%4 
            elif command == -2:
                di = (di+1)%4 
            else:    
                for i in range(command): 
                    if (x+dx[di], y+dy[di]) not in d:
                        x, y = x+dx[di], y+dy[di] 
                    else: 
                        break
                res = max(res, x**2 + y**2)         
                        
        return res
