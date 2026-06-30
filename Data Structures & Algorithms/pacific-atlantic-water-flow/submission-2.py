class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n_rows = len(heights)
        n_cols = len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def bfs(queue):
            visited = set(queue)
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # Check bounds, if not visited, and if water can flow UPHILL
                    if 0 <= nr < n_rows and 0 <= nc < n_cols and (nr, nc) not in visited:
                        if heights[nr][nc] >= heights[r][c]:
                            queue.append((nr, nc))
                            visited.add((nr, nc))
            return visited

        # Seed the queues with the coastal cells
        pacific_q = deque([(r, 0) for r in range(n_rows)] + [(0, c) for c in range(n_cols)])
        atlantic_q = deque([(r, n_cols - 1) for r in range(n_rows)] + [(n_rows - 1, c) for c in range(n_cols)])

        # Run BFS for both oceans
        pacific_visited = bfs(pacific_q)
        atlantic_visited = bfs(atlantic_q)

        # Return the intersection of both sets
        return [list(cell) for cell in (pacific_visited & atlantic_visited)]
        