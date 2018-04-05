class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while(val in nums):
            nums.remove(val)
        return len(nums)

a = [3,2,2,3]
print Solution().removeElement(a, 3)
print a