from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        queue = deque([])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n_rows = len(grid)
        n_cols = len(grid[0])

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 2:
                    queue.append([r, c])

        res = -1
        while queue:
            length = len(queue)
            for _ in range(length):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
                        queue.append([nr, nc])
                        grid[nr][nc] = 2
            res += 1

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    return -1
        return res if res > 0 else 0