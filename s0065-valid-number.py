class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return float(s)


print Solution().isNumber(".2e10")