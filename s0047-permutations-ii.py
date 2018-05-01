from itertools import permutations

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l = [list(x) for x in permutations(nums)]
        temp_list = list(set([str(i) for i in l]))
        return [eval(i) for i in temp_list]

print Solution().permuteUnique([1,1,2])