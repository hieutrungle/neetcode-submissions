class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        n_rows = len(heights)
        n_cols = len(heights[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        queue = deque([])
        visited = set()
        for r in range(n_rows):
            queue.append([r, n_cols - 1])
            visited.add((r, n_cols - 1))
        for c in range(n_cols):
            queue.append([n_rows - 1, c])
            visited.add((n_rows - 1, c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols and heights[nr][nc] >= heights[r][c]:
                    if (nr, nc) not in visited:
                        queue.append([nr, nc])
                        visited.add((nr, nc)) 
        
        queue2 = deque([])
        visited2 = set()
        for r in range(n_rows):
            queue2.append([r, 0])
            visited2.add((r, 0))
        for c in range(n_cols):
            queue2.append([0, c])
            visited2.add((0, c))

        while queue2:
            r, c = queue2.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols and heights[nr][nc] >= heights[r][c]:
                    if (nr, nc) not in visited2:
                        queue2.append([nr, nc])
                        visited2.add((nr, nc))

        visited = visited & visited2
        return [list(v) for v in visited]
        