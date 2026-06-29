from collections import deque

class UnionFind:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for _ in range(n)]

    def find(self, u):
        if u == self.parents[u]:
            return self.parents[u]

        self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.sizes[u] > self.sizes[v]:
            root_u, root_v = root_v, root_u
        
        self.parents[root_v] = root_u
        self.sizes[root_u] += self.sizes[root_v]
        return True


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        n_rows = len(grid)
        n_cols = len(grid[0])

        def get_index(r, c):
            return r + c * n_rows

        uf = UnionFind(n_rows * n_cols)
        res = 0

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n_rows and 0 <= nc < n_cols and grid[nr][nc] == 1:
                            uf.union(get_index(r, c), get_index(nr, nc))
                    res = max(uf.sizes)
        return res
