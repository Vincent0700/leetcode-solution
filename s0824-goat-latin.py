class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        l = S.split(' ')
        for i in range(len(l)):
            item = l[i]
            if item[0].lower() in list("aeiou"):
                l[i] += "ma"
            else: l[i] = item[1:] + item[0] + "ma"
            l[i] += (i+1)*'a'
        return ' '.join(l)

print Solution().toGoatLatin("I speak Goat Latin")