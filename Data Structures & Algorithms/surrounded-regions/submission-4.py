from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        queue = deque([])
        n_rows = len(board)
        n_cols = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for r in range(n_rows):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][n_cols - 1] == 'O':
                queue.append((r, n_cols - 1))
            
        for c in range(1, n_cols - 1):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[n_rows - 1][c] == 'O':
                queue.append((n_rows - 1, c))
        stays = set(queue)
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n_rows and 0 <= nc < n_cols and board[nr][nc] == "O" and (nr, nc) not in stays:
                    stays.add((nr, nc))
                    queue.append((nr, nc))

        for r in range(n_rows):
            for c in range(n_cols):
                if (r, c) not in stays:
                    board[r][c] = 'X'

            