import re

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return True if re.search("^"+p+"$", s) else False


print Solution().isMatch("aa", "a")
