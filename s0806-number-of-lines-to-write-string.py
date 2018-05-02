class Solution(object):
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        row = 1
        end = 0
        for c in S:
            w = widths[(ord(c)-ord('a'))]
            if end+w > 100:
                row += 1
                end = w
            else: 
                end += w
        return [row, end]

print Solution().numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], "abcdefghijklmnopqrstuvwxyz")