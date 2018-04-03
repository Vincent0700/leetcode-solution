class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        maxlen = 0
        maxstr = ""
        n = len(s)
        if(n == 1):
            return s[0]
        for i in range(n):
            for j in range(i, n+1):
                ss = s[i:j]
                if(self.isPalindrome(ss) and j-i > maxlen):
                    maxlen = j-i
                    maxstr = ss
        return maxstr

    def isPalindrome(self, s):
        n = len(s)
        flag = True
        for i in range(n/2):
            if(s[i] <> s[n-1-i]):
                flag = False
        return flag

print Solution().longestPalindrome("aa")