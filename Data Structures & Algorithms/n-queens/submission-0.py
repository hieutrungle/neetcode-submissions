class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        cols = [False] * n
        pos_diag = [False] * (n * 2)
        neg_diag = [False] * (n * 2)

        def dfs(r):
            if r >= n:
                self.res.append(["".join(ele) for ele in board])
                return
            
            for c in range(n):
                if cols[c] or pos_diag[r + c] or neg_diag[r - c + n]:
                    continue
                board[r][c] = 'Q'
                cols[c] = True
                pos_diag[r + c] = True
                neg_diag[r - c + n] = True
                dfs(r + 1)
                cols[c] = False
                pos_diag[r + c] = False
                neg_diag[r - c + n] = False
                board[r][c] = '.'
            return

        dfs(0)
        return self.res