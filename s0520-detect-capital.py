import re

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return re.match(r'^[A-Z]+$|^[a-z]+$|^[A-Z][a-z]+$', word) != None

print Solution().detectCapitalUse("Flag")