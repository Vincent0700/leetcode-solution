class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        c = len(matrix)
        tmp = [[0 for x in range(c)] for x in range(c)]
        for i in range(c):
            for j in range(c):
                tmp[i][j] = matrix[c-1-j][i]
        for i in range(c):
            for j in range(c):
                matrix[i][j] = tmp[i][j]


mat = [[1,2,3],[4,5,6],[7,8,9]]
Solution().rotate(mat)
print mat
