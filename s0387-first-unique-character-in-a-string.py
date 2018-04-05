class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = []
        nums = []
        first_id = []
        for i in range(len(s)):
            c = s[i]
            count = table.count(c)
            if count == 0:
                table.append(c)
                nums.append(1)
                first_id.append(i)
            else:
                index = table.index(c)
                nums[index] += 1
        for i in range(len(nums)):
            if(nums[i] == 1):
                return first_id[i]
        return -1


print Solution().firstUniqChar("loveleetcode")
