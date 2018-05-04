class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        tmp = [len(x)*[0x7fffffff] for x in matrix]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    tmp[i] = len(matrix[i]) * [0]
                    for k in range(len(matrix)):
                        tmp[k][j] = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if tmp[i][j] == 0:
                    matrix[i][j] = 0


matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
Solution().setZeroes(matrix)
print matrix
