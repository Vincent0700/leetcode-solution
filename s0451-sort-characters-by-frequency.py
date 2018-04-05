class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        table = []
        nums = []
        for i in range(len(s)):
            c = s[i]
            count = table.count(c)
            if count == 0:
                table.append(c)
                nums.append(1)
            else:
                index = table.index(c)
                nums[index] += 1
        l = list(s)
        l.sort()
        l.sort(lambda x,y: nums[table.index(y)] - nums[table.index(x)])
        return "".join(l)

print Solution().frequencySort("loveleetcode")