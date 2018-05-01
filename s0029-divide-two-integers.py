class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 0x7fffffff
        if divisor == 0:
            return MAX_INT
        a = abs(dividend) / abs(divisor)
        a = -a if dividend ^ divisor < 0 else a
        a = a if a <= MAX_INT else MAX_INT
        return a