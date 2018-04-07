tri = [[1]]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        global tri
        if(numRows <= len(tri)):
            return tri[:numRows]
        while(numRows > len(tri)):
            a = tri[-1]
            tri.append([a[i] + a[i-1] if i > 0 else a[i] for i in range(len(a))] + [1])
        return tri


print Solution().generate(5)
        
