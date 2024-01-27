class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        l=len(s)
        res=''
        if numRows == 1:
            return s
        for i in range(numRows):
            temp=i
            while (temp<l):
                res+=s[temp]
                if (i==0 or i==numRows-1):
                    temp=temp+(numRows-1)*2 
                else:
                    if (temp+(numRows-i-1)*2<l):
                        res+=s[temp+(numRows-i-1)*2]
                    temp+=(numRows-1)*2

        return res
