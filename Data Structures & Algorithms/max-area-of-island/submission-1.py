from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n_rows = len(grid)
        n_cols = len(grid[0])

        def bfs(r, c):
            queue = deque([[r, c]])
            cnt = 0
            while queue:
                r, c = queue.popleft()
                cnt += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        queue.append([nr, nc])
                
            return cnt

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    res = max(res, bfs(r, c))

        return res