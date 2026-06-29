class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.res = 0

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n_rows = len(grid)
        n_cols = len(grid[0])

        def dfs(r, c):
            if not 0 <= r < n_rows or not 0 <= c < n_cols or not grid[r][c] == "1":
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

            return

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == "1":
                    self.res += 1
                    dfs(r, c)
        
        return self.res