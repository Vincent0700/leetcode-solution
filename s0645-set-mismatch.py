from collections import Counter

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        dup = [x for x in counter if counter[x] > 1][0]
        mis = list(set(range(1, len(nums)+1)) - set(nums))[0]
        return [dup, mis]


print Solution().findErrorNums([1, 2, 2, 4])
