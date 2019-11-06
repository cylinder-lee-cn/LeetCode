"""
54. 螺旋矩阵

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]

示例 2:
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        if (rows == 0):
            return matrix
        if (rows == 1):
            return matrix[0]

        cols = len(matrix[0])
        result = []
        top, bottom, left, right = 1, rows - 1, 0, cols - 1

        r, c = 0, 0

        # go = ['r','l','u','d']  # 方向 右、左、上、下
        way = 'r'

        for i in range(cols * rows):
            result.append(matrix[r][c])
            # print(matrix[r][c])
            if (way == 'r'):  # 向右走
                if (c < right):
                    c = c + 1
                else:
                    c = right
                    right = right - 1
                    r = r + 1
                    way = 'd'
            elif (way == 'l'):
                if (c > left):
                    c = c - 1
                else:
                    c = left
                    left = left + 1
                    way = 'u'
                    r = r - 1
            elif (way == 'u'):
                if (r > top):
                    r = r - 1
                else:
                    r = top
                    top = top + 1
                    way = 'r'
                    c = c + 1
            elif (way == 'd'):
                if (r < bottom):
                    r = r + 1
                else:
                    r = bottom
                    bottom = bottom - 1
                    way = 'l'
                    c = c - 1

        return result


s = Solution()
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
"""
此题解法：
* 简单粗暴的方式，定义4个方向：右-下-左-上，这个就是螺旋走向，然后开始走
* 预先定义4个边界，top，bottom，left，right
* 按照方向走，首先是向右走，就判断是否到了right，如果是就向下走，而且右边界缩减1
* 向下走如果到了bottom，那就向左走，bottom向上移动1
* 向左走如果到了left，那么就向上走，而且left增1
* 向上走如果到top，那就向右走，而且top增1
"""
