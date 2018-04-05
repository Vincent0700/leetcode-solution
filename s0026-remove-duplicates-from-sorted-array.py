class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = sorted(set(nums), key=nums.index)
        del nums [:]
        nums.extend(tmp)
        return len(tmp)

print Solution().removeDuplicates([1,1,2,2,3,3,3])