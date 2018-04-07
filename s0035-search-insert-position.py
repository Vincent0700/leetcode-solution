class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return len([x for x in nums if x < target])


print Solution().searchInsert([1, 3, 5, 6], 5)
print Solution().searchInsert([1, 3, 5, 6], 2)
print Solution().searchInsert([1, 3, 5, 6], 7)
print Solution().searchInsert([1, 3, 5, 6], 0)
