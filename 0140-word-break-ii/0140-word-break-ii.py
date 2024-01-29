class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        root ={}

        for word in wordDict:
            cur =root
            for c in word:
                if c not in cur:
                    cur[c ] ={}
                cur =cur[c]
            cur['']={}
        def dp(s,k,n):
            cur=root
            result=[]
            for i in range(k, n):
                if '' in cur:
                    x=dp(s, i, n)
                    if x:
                        for r in x:
                            result.append(s[k:i]+' '+r)
                if s[i] in cur:
                    cur=cur[s[i]]
                else:
                    return result
            if '' in cur:
                result.append(s[k:])
            return result
        n=len(s)
        return(dp(s,0,n))
