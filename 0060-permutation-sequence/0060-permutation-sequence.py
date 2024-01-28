class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        result=[]
        arr=[i+1 for i in range(n)]
        fact=[1]*n
        for i in range(2,n):
            fact[i]=fact[i-1]*i
        j=n-1
        while j!=-1:
            result.append(arr[(k-1)//fact[j]])
            arr.remove(arr[(k-1)//fact[j]])
            k=(k-1)%fact[j]+1
            j-=1
        return ''.join(map(str,result))
        
            