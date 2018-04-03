class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = []
        minint = -0x80000000
        while(len(nums1) > 0 or len(nums2) > 0):
            val1 = val2 = minint
            len1 = len(nums1)
            len2 = len(nums2)
            if(len1 > 0):
                val1 = nums1[len1-1]
            if(len2 > 0):
                val2 = nums2[len2-1]
            if(val1 > val2):
                nums1.pop()
                l.append(val1)
            else:
                nums2.pop()
                l.append(val2)
        len3 = len(l)
        mid = 0
        if(len3 % 2):
            mid = l[len3/2]
        else:
            mid = (l[len3/2-1]+l[len3/2])/2.0
        return mid


