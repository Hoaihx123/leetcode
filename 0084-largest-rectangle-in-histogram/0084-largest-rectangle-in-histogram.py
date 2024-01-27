class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        rmp=[0]*n
        lmp=[0]*n
        s=[]
        for i in range(n):
            while s and heights[i]<=heights[s[-1]]:
                s.pop()
            if s:
                rmp[i]=s[-1]
            else:
                rmp[i]=-1
            s.append(i)
        s=[]
        for i in range(n-1, -1,-1):
            while s and heights[i]<=heights[s[-1]]:
                s.pop()
            if s:
                lmp[i]=s[-1]
            else:
                lmp[i]=n
            s.append(i)
        result=0
        for i in range(n):
            result=max(result,heights[i]*(lmp[i]-rmp[i]-1))
        return result
        