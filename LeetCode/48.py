"""
48. 旋转图像

给定一个 n × n 的二维矩阵表示一个图像。
将图像顺时针旋转 90 度。

说明：
你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:
给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

示例 2:
给定 matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
],

原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]

"""


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        x = len(matrix[0])
        y = len(matrix)

        for i in range(y):
            for j in range(i, x):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            for k in range(x // 2):
                matrix[i][k], matrix[i][x - 1 - k] = matrix[i][x - 1 -
                                                               k], matrix[i][k]

        print(matrix)


s = Solution()
s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
"""
此题解法：
* 顺时针旋转90度，首先将数组的行、列转换，然后翻转每一行，就是最后的结果
* 比如
[1,2,3],
[4,5,6],
[7,8,9]
首先行列转换就是
[1，4，7]
[2，5，8]
[3，6，9]
然后每行翻转
[7，4，1]
[8，5，2]
[9，8，3]

一句话版本
matrix = [x[::-1] for x in zip(*matrix)]

难度就在只允许修改当前数组，不允许用另外的数组来旋转
"""
