from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        n_rows = len(grid)
        n_cols = len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        queue = deque([])
        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 0:
                    queue.append([r, c])

        step = 0
        while queue:
            length = len(queue)
            step += 1
            for _ in range(length):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = step
                        queue.append([nr, nc])