class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m, n = len(board), len(board[0])
        dr = [0, -1, -1]
        dc = [-1, 0, -1]
        p = 10**9 + 7
        reward = [[0]*n for _ in range(m)]
        paths = [[0]*n for _ in range(m)]
        paths[m-1][n-1] = 1
        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if paths[r][c] == 0:
                    continue
                for d in range(3):
                    nr, nc = r+dr[d], c+dc[d]
                    if nr < 0 or nc < 0 or board[nr][nc] == 'X':
                        continue
                    nsum = reward[r][c]
                    if board[nr][nc] != 'E':
                        nsum += int(board[nr][nc])
                    if nsum > reward[nr][nc]:
                        reward[nr][nc] = nsum
                        paths[nr][nc] = paths[r][c]
                    elif nsum == reward[nr][nc]:
                        paths[nr][nc] += paths[r][c]
                    
        return [reward[0][0]%p, paths[0][0]%p]
