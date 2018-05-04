class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1 = list(set([x for x in nums if x > 0]))
        if len(s1) == 0:
            return 1
        minNum = min(s1)
        if minNum > 1:
            return 1
        maxNum = max(s1)
        s2 = sorted(s1)
        if maxNum - minNum + 1 == len(s2):
            return maxNum + 1
        s3 = range(minNum, maxNum+1)
        for i in range(len(s2)):
            if s2[i] != s3[i]:
                return s3[i]


print Solution().firstMissingPositive([7, 8, 9, 11, 12])
