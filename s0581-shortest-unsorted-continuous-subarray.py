class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        i = 0
        j = len(a)-1
        while(i < len(a) and a[i] == nums[i]):
            i += 1
        while(j > -1 and a[j] == nums[j]):
            j -= 1
        if(j > i):
            return j-i+1
        else:
            return 0

print Solution().findUnsortedSubarray([1,2,3,5,4])