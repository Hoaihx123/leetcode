class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def check(row, col, value):
            for i in range(9):
                if board[row][i]==value:
                    return False
                if board[i][col]==value:
                    return False
                if board[3*(row//3)+i//3][3*(col//3)+i%3]==value:
                    return False
            return True
        def solve(row, col):
            if row==9:
                return True
            if col==9:
                return solve(row+1, 0)
            if board[row][col]=='.':
                for i in range(1,10):
                    if check(row,col,str(i)):
                        board[row][col]=str(i)
                        if solve(row,col+1):
                            return True
                        else:
                            board[row][col]='.' 
                return False
            return solve(row, col+1)
        solve(0,0)
                    
                    

                