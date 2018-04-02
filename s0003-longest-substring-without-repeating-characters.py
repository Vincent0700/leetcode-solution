class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = j = maxlen = 0
        while(j < len(s)):
            j += 1
            tmp = s[i:j]
            if(tmp.count(s[j-1]) == 1):
                maxlen = max(maxlen, len(tmp))
            else:
                i = i + tmp.find(s[j-1]) + 1
        return maxlen

