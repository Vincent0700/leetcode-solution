tri = [[1]]


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        global tri
        if(rowIndex < len(tri)):
            return tri[rowIndex]
        while(rowIndex > len(tri)-1):
            a = tri[-1]
            tri.append([a[i] + a[i-1] if i > 0 else a[i]
                        for i in range(len(a))] + [1])
        return tri[rowIndex]


print Solution().getRow(4)
