class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m=len(t)
        n=len(s)
        l1=[1]*(n+1)
        l2=[0]*(n+1)
        for i in range(m):
            for j in range(n):
                if s[j]==t[i]:
                    l2[j+1]=l1[j]+l2[j]
                else:
                    l2[j+1]=l2[j]
            l1=l2[:]
            l2=[0]*(n+1)

        return(l1[-1])