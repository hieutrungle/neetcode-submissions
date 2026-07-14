class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        n_rows, n_cols = len(matrix), len(matrix[0])
        
        # Step 1: Check if the first row or first column have any zeros
        first_row_0 = any(matrix[0][c] == 0 for c in range(n_cols))
        first_col_0 = any(matrix[r][0] == 0 for r in range(n_rows))
        
        # Step 2: Use the first row and first column to mark zero rows and columns
        for r in range(1, n_rows):
            for c in range(1, n_cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                    
        # Step 3: Zero out the inner matrix based on the markers
        for r in range(1, n_rows):
            for c in range(1, n_cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # Step 4: Zero out the first column if needed
        if first_col_0:
            for r in range(n_rows):
                matrix[r][0] = 0
                
        # Step 5: Zero out the first row if needed
        if first_row_0:
            for c in range(n_cols):
                matrix[0][c] = 0
