def construct(self, grid):
	if not grid: return None
	if self.isLeaf(grid):
		return Node(grid[0][0] == 1, True, None, None, None, None)
	n = len(grid)
	return Node('*',
				False,
				self.construct([row[:n/2] for row in grid[:n/2]]),
				self.construct([row[n/2:] for row in grid[:n/2]]),
				self.construct([row[:n/2] for row in grid[n/2:]]),
				self.construct([row[n/2:] for row in grid[n/2:]]))

def isLeaf(self, grid):
    return all(grid[i][j] == grid[0][0] 
        for i in range(len(grid)) for j in range(len(grid[i])))
