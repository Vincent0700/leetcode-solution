class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp = [''.join(sorted(x)) for x in strs]
        tmp2 = [tmp.index(x) for x in tmp]
        tmp3 = [[x,y] for x,y in zip(tmp2, strs)]
        tmp4 = [[x[0], []] for x in tmp3]
        for i in range(len(tmp3)):
            index = tmp3[i][0]
            val = tmp3[i][1]
            tmp4[index][1].append(val)
        for i in range(len(tmp4)-1, -1, -1):
            if len(tmp4[i][1]) == 0:
                tmp4.remove(tmp4[i])
        tmp5 = [x[1] for x in tmp4]
        return tmp5


print Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
