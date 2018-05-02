from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = [[]]
        l += [[x] for x in nums]
        for i in range(1, len(nums)):
            l += [list(x) for x in combinations(nums, i+1)]
        return l

print Solution().subsets([1,2,3])