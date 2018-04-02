#!/usr/bin/python


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i <> j and nums[i] + nums[j] == target):
                    result = []
                    result.append(i)
                    result.append(j)
                    return result



print Solution().twoSum([2, 0, 7, 5], 9)
