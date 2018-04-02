class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        flag = [False for i in range(length)]
        for i in range(length):
            a = nums[i]
            if(a >= 1 and a <= length):
                flag[a-1] = True
        result = []
        for i in range(length):
            if(flag[i] == False):
                result.append(i+1)
        return result

print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])