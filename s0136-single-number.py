from collections import Counter

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for n in counter:
            if counter[n] == 1:
                return n


print Solution().singleNumber([4,1,2,1,2])
