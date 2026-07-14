class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n_rows, n_cols = len(matrix), len(matrix[0])
        d = 0
        cur = [0, 0]
        res = []

        while len(res) < n_cols * n_rows:
            r, c = cur
            res.append(matrix[r][c])
            matrix[r][c] = float('inf')
            nr, nc = r + directions[d][0], c + directions[d][1]
            if not 0 <= nr < n_rows or not 0 <= nc < n_cols or matrix[nr][nc] == float('inf'):
                d = (d + 1) % 4
                nr, nc = r + directions[d][0], c + directions[d][1]
            cur = [nr, nc]

        return res
            