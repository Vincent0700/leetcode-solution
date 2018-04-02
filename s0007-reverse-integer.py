class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        tmp = str(x)
        negative = False
        if(tmp[0] == "-"):
            tmp = tmp[1:len(tmp)]
            negative = True
        l = list(tmp)
        l.reverse()
        num = int(("-" if negative else "") + "".join(l))
        return num if num >= -2147483648 and num <= 2147483647 else 0

print Solution().reverse("1534236469")
