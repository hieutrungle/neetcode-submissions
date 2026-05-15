class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        t, b = 0, n_rows - 1
        while t <= b:
            m = (t + b) // 2
            if matrix[m][0] <= target <= matrix[m][-1]:
                t = m
                break
            elif target < matrix[m][0]:
                b = m - 1
            else:
                t = m + 1

        if t >= n_rows:
            return False
            
        row = t
        l, r = 0, n_cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True

        return False