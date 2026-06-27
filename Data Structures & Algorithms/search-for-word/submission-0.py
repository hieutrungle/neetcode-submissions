class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n_rows = len(board)
        n_cols = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(r, c, w_idx):
            if w_idx >= len(word):
                return True

            if not 0 <= r < n_rows or not 0 <= c < n_cols or board[r][c] != word[w_idx]:
                return False

            # valid character
            board[r][c] = '.'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs(nr, nc, w_idx + 1):
                    return True
            board[r][c] = word[w_idx]
            return False

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False
        