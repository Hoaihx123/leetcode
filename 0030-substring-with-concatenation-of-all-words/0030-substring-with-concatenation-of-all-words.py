class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m = len(words[0])
        n = len(words)
        l = len(s)
        dict1 = {}
        result = []
        for w in words:
            dict1[w] = dict1.get(w, 0) + 1
        for i in range(m):
            start = i
            dict2={}
            count=0
            for j in range(i, l-m+1, m):
                temp=s[j:j+m]
                if temp in dict1:
                    dict2[temp]=dict2.get(temp,0)+1
                    count+=1
                    while dict2[temp]>dict1[temp]:
                        dict2[s[start:start+m]]-=1
                        start+=m
                        count-=1
                    if count==n:
                        result.append(start)
                else:
                    start=j+m
                    dict2={}
                    count=0 
        return result

