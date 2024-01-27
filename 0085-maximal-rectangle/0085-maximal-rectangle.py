class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def maxRec(arr,n):
            rmp=[-1]*n
            lmp=[n]*n
            s=[]
            for i in range(n):
                while s and arr[s[-1]]>=arr[i]:
                    s.pop()
                if s:
                    rmp[i]=s[-1]
                s.append(i)
            s=[]
            for i in range(n-1, -1, -1):
                while s and arr[s[-1]]>=arr[i]:
                    s.pop()
                if s:
                    lmp[i]=s[-1]
                s.append(i)
            result=0
            for i in range(n):
                result=max(result, arr[i]*(lmp[i]-rmp[i]-1))
            return result
        m=len(matrix)
        n=len(matrix[0])
        arr=[0]*n
        max_rect=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=="0":
                    arr[j]=0
                else:
                    arr[j]+=1
            max_rect=max(max_rect, maxRec(arr, n))
        return max_rect