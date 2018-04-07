length = 1
arr = ["1"]


class Solution(object):

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        global length, arr
        if(n <= length):
            return arr[n-1]
        while(length < n):
            s = arr[length-1]
            l = []
            l.append((s[0], 1))
            for i in range(1, len(s)):
                if s[i] == l[-1][0]:
                    l[-1] = (l[-1][0], l[-1][1]+1)
                else:
                    l.append((s[i], 1))

            l = [str(t[1])+str(t[0]) for t in l]
            arr.append("".join(l))
            length += 1
        return arr[n-1]


print Solution().countAndSay(1)
print Solution().countAndSay(2)
print Solution().countAndSay(3)
print Solution().countAndSay(4)
print Solution().countAndSay(5)
