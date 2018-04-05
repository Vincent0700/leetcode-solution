class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        l = []
        flag = True
        while(flag):
            c = ""
            for i in range(len(strs)):
                if len(strs[i]) == 0:
                    flag = False
                    break
                if(c == ""):
                    c = strs[i][0]
                elif strs[i][0] <> c:
                    flag = False
                    break
                strs[i] = strs[i][1:]
            if flag:
                l.append(c)
        return "".join(l)

print Solution().longestCommonPrefix(["aa", "a"])