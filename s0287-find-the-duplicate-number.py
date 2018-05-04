from collections import Counter

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = Counter(nums)
        return [x for x in l if l[x] > 1][0]


print Solution().findDuplicate([1, 2, 3, 1])
