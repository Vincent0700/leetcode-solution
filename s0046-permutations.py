from itertools import permutations

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [list(x) for x in permutations(nums)]

print Solution().permute([1,2,3])
        