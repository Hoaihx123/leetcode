class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        def recusive(i,j):
            if count[i][j]==0:
                count[i][j]=1+max(recusive(i-1,j) if i > 0 and matrix[i][j] < matrix[i-1][j] else 0, 
                                  recusive(i+1,j) if i <m-1 and matrix[i][j] < matrix[i+1][j] else 0,
                                  recusive(i,j-1) if j > 0 and matrix[i][j] < matrix[i][j-1] else 0,
                                  recusive(i,j+1) if j <n-1 and matrix[i][j] < matrix[i][j+1] else 0,0)
            return count[i][j]
        
        count = [[0 for _ in range(n)] for _ in range(m)]
        result=0
        for i in range(m):
            for j in range(n):
                result=max(result,recusive(i,j))
        return result
        
                