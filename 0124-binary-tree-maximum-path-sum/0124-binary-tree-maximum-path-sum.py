# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, r):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dp(root):
            if root.left is None and root.right is None:
                return [root.val, max(root.val,0)]
            if root.left is None:
                result=dp(root.right)
                return [max(result[0], result[1]+root.val), max(result[1]+root.val,0)]
            if root.right is None:
                result=dp(root.left)
                return [max(result[0], result[1]+root.val),max(result[1]+root.val,0)]
            lf=dp(root.left)
            rh=dp(root.right)
            return [max(lf[0],rh[0],lf[1]+root.val+rh[1]), max(lf[1]+root.val,rh[1]+root.val,0)]
        return dp(r)[0]
        