class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x < 0): 
            return False
        tmp = list(str(x))
        tmp.reverse()
        rx = int("".join(tmp))
        return x == rx

print Solution().isPalindrome(123321)
        