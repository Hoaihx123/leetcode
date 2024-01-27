class Solution(object):
    def isRepeating(self, string):
        l = len(string)
        for i in range(l-1):
            for j in range(i+1,l):
                if string[i]==string[j]:
                    return True
        return False

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if(length == 0):
            return 0
        resul = 1
        for i in range(1,length):
            if(self.isRepeating(s[i-resul:i+1])==0):
                resul += 1
        return resul