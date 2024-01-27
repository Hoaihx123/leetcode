class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        ln=[0]*n
        rn=[0]*n
        for i in range(1,n):
            ln[i]=ln[i-1]+1 if ratings[i]>ratings[i-1] else 0
            rn[n-i-1]=rn[n-i]+1 if ratings[n-i-1]>ratings[n-i] else 0
        s=0
        for i in range(n):
            s+=max(ln[i],rn[i])+1
        return s