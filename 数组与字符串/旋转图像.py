'''
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

'''
# 思路:矩阵顺时针旋转90 度  等于矩阵转置后乘一个常数矩阵,单位矩阵的转置矩阵

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]




if __name__ == '__main__':
    matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
    solute = Solution()
    print(solute.rotate(matrix))