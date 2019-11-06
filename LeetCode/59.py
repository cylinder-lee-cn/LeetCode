"""
59. 螺旋矩阵 II

给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。

示例:

输入: 3
输出:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if (n == 0):
            return []
        if (n == 1):
            return [1]

        rows = cols = n
        top, bottom, left, right = 1, rows - 1, 0, cols - 1
        r, c = 0, 0
        way = 'r'
        matrix = [[None] * n for i in range(n)]
        for i in range(1, cols * rows + 1):
            matrix[r][c] = i
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

        return matrix


s = Solution()
print(s.generateMatrix(3))
"""
此题解法：
* 初始化一个N×N的二维数组
* 然后采取54题的走法依次更新元素的值即可
"""
