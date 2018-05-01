import re

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            a = re.search(r"^[+-]?\d+", str).group()
            a = int(a)
            a = a if a >= -2147483648 else -2147483648
            a = a if a <= 2147483647 else 2147483647
        except:
            a = 0
        return a

print Solution().myAtoi("  010")