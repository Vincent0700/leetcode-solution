class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        t1 = nums1[0:m]
        t2 = nums2[0:n]
        del nums1[:]
        nums1.extend(t1)
        nums1.extend(t2)
        nums1.sort()