class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0:
            return
        pal = [[False]*length for _ in range(length)]
        for i in range(length):
            pal[i][i] = True
        if length == 1:
            return s
        max = 1
        resul = [0, 1]
        for L in range(2, length+1):
            for i in range(length-L+1):
                if (s[i]==s[i+L-1]) and ((L==2) or (pal[i+1][i+L-2])):
                    pal[i][i+L-1] = True 
                    if L>max:
                        max = L
                        resul = [i, i+L]
        return s[resul[0]:resul[1]]
        