class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        result=1
        for i in range(m - 1):
            result *= (m + n - 2 - i)
        for i in range(m-1):
            result//=(i+1)
        return result