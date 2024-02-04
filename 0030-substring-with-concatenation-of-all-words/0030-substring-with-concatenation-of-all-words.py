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
            while start + m * n <= l:
                dict2 = {}
                j=start
                while j <start+m*n:
                    temp=s[j:j + m]
                    if dict1.get(temp, 0) > dict2.get(temp, 0):
                        dict2[temp] = dict2.get(temp, 0) + 1
                        j+=m
                    else:
                        break
                if j < start + m * n:
                    if dict1.get(temp):
                        start += m
                    else:
                        start = j + m
                else:
                    result.append(start)
                    start += m
        return result

