class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n = len(s)
        m = len(p)
        dp = [[False for _ in range(m+1)] for _ in range(n+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[0][i] = p[i-1] == '*' and dp[0][i-1]
        for i in range(1, n+1):
            for j in range(1, m+1):
                if p[j-1] == '?' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
        return dp[n][m]