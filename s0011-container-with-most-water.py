class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxvol = 0
        while(i <= j):
            h1 = height[i]
            h2 = height[j]
            hmin = min(h1, h2)
            vol = hmin * (j - i)
            if(vol > maxvol):
                maxvol = vol
            if(h1 == hmin):
                i += 1
            else:
                j -= 1
        return maxvol
    
print Solution().maxArea([1,2,3,4])
