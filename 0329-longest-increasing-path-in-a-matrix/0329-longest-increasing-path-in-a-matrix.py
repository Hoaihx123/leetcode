class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        def findMax(matrix,m,n,max_before):
            max_value=float('-inf')
            index=[]
            for i in range(m):
                for j in range(n):
                    if matrix[i][j]>max_value and matrix[i][j]<max_before:
                        max_value=matrix[i][j]
                        index=[(i,j)]
                    elif matrix[i][j]==max_value:
                        index.append((i,j))
            return {'index': index, 'max_value': max_value}
        m = len(matrix)
        n = len(matrix[0])
        count = [[None for _ in range(n)] for _ in range(m)]
        max_before = float('inf')
        fm = findMax(matrix, m, n, max_before)
        result=0
        while fm['index']:
            for u in fm['index']:
                point = None
                longest = 1
                if u[0] > 0 and matrix[u[0]][u[1]] < matrix[u[0] - 1][u[1]]:
                    longest = 1 + count[u[0] - 1][u[1]][0]
                    point = (u[0] - 1, u[1])
                if u[0] < m - 1 and matrix[u[0]][u[1]] < matrix[u[0] + 1][u[1]]:
                    if count[u[0] + 1][u[1]][0] + 1 > longest:
                        longest = 1 + count[u[0] + 1][u[1]][0]
                        point = (u[0] + 1, u[1])
                if u[1] > 0 and matrix[u[0]][u[1]] < matrix[u[0]][u[1] - 1]:
                    if count[u[0]][u[1] - 1][0] + 1 > longest:
                        longest = 1 + count[u[0]][u[1] - 1][0]
                        point = (u[0], u[1] - 1)
                if u[1] < n - 1 and matrix[u[0]][u[1]] < matrix[u[0]][u[1] + 1]:
                    if count[u[0]][u[1] + 1][0] + 1 > longest:
                        longest = 1 + count[u[0]][u[1] + 1][0]
                        point = (u[0], u[1] + 1)
                result=max(longest,result)
                count[u[0]][u[1]] = (longest, point)
            fm = findMax(matrix, m, n, fm['max_value'])
        return result
        
                