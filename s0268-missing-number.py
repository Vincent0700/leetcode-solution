class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = range(len(nums)+1)
        for i in nums:
            l[i] = -1
        for i in l:
            if l[i] != -1:
                return l[i]


print Solution().missingNumber([3, 0, 1])
