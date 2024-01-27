class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        max=[0]*n
        max_value=0
        for i in range(n):
            if height[i]>max_value:
                max_value=height[i]
            max[i]=max_value
        max_value=0
        s=0
        for i in range(n-1,-1,-1):
            if height[i]>max_value:
                max_value=height[i]
            max[i]=min(max_value, max[i])
            s+=max[i]-height[i]
        return s
                