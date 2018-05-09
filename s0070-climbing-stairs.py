result = [1, 2]

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        global result
        if len(result) >= n:
            return result[n-1]
        else:
            for i in range(len(result), n):
                result.append(result[i-2]+result[i-1])
            return result[n-1]


print Solution().climbStairs(5)
