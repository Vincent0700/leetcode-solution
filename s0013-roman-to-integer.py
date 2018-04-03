class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = ["MMM", "MM", "M", "CM", "DCCC", "DCC", "DC", "D",
             "CD", "CCC", "CC", "C", "XC", "LXXX", "LXX", "LX", "L",
             "XL", "XXX", "XX", "X", "IX", "VIII", "VII", "VI", "V",
             "IV", "III", "II", "I"]
        b = [3000, 2000, 1000, 900, 800, 700, 600, 500,
             400, 300, 200, 100, 90, 80, 70, 60, 50,
             40, 30, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        num = 0
        for i in range(len(a)):
            if(s.find(a[i]) == 0):
                s = s[len(a[i]): len(s)]
                num += b[i]
        return num


print Solution().romanToInt("MCMXCVI")
