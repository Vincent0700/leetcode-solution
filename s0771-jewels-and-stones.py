class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return sum([list(S).count(x) for x in list(J)])


print Solution().numJewelsInStones("z", "ZZ")
