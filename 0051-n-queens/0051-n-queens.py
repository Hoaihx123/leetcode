class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        matrix = ['.'*n]*n
        def check(matrix, row, col):
            for i in range(n):
                if matrix[i][col]=='Q' or matrix[row][i]=='Q':
                    return False
                if (col-i)+row<n and col-i+row>=0 and matrix[col-i+row][i]=='Q':
                    return False
                if row-col+i<n and row-col+i>=0 and matrix[row-col+i][i]=='Q':
                    return False
            return True

        def solve(row, matrix, result):
            if row == n:
                result.append(matrix[:])
                return result
            for col in range(n):
                if check(matrix, row, col):
                    matrix[row] = matrix[row][0:col]+'Q'+matrix[row][col+1:n]
                    result = solve(row+1, matrix, result)
                    matrix[row] = matrix[row][0:col]+'.'+matrix[row][col+1:n]
            return result
        return solve(0, matrix, [])
        