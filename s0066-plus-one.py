class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        return [int(x) for x in list(str(int(''.join([str(x) for x in digits]))+1))]


print Solution().plusOne([1, 2, 3])
