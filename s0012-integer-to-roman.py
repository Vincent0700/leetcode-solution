class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        a = ["MMM", "MM", "M", "CM", "DCCC", "DCC", "DC", "D",
             "CD", "CCC", "CC", "C", "XC", "LXXX", "LXX", "LX", "L",
             "XL", "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V",
             "IV", "III", "II", "I"]
        l = []
        t = num / 1000
        if(t > 0):
            l.append(a[3-t])
        t = (num % 1000) / 100
        if(t > 0):
            l.append(a[12-t])
        t = (num % 100) / 10
        if(t > 0):
            l.append(a[21-t])
        t = num % 10
        if(t > 0):
            l.append(a[30-t])
        return "".join(l)

print Solution().intToRoman(1996)