"""
498. 对角线遍历

给定一个含有 M x N 个元素的矩阵（M 行，N 列），
请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

示例:
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]

解释: 498-1.png

说明:
给定矩阵中的元素总数不会超过 100000 。

"""


class Solution:
    def findDiagonalOrder(self, matrix):
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
        r, c = 0, 0
        for i in range(cols * rows):
            result.append(matrix[r][c])
            if ((r + c) % 2 == 0):
                if (r == 0 and c != cols - 1):
                    c = c + 1  # 元素在第一行，往右走
                elif (c == cols - 1):
                    r = r + 1  # 元素在最后一列，往下走
                else:  # 其他情况，往右上走
                    r = r - 1
                    c = c + 1
            else:
                if (c == 0 and r != rows - 1):
                    r = r + 1  # 元素在第一列，往下走
                elif (r == rows - 1):
                    c = c + 1  # 在最后一行，往右走
                else:  # 其他情况，往左下走
                    r = r + 1
                    c = c - 1
        return result


s = Solution()
# s.findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(s.findDiagonalOrder([[1, 2], [3, 4]]))
"""
此题解法：
* 对角线访问，如果做一个水平移动的话就是每一行都向后平移一个位置
    1,2,3
      4,5,6
        7,8,9
* 然后按列读取，注意0，2，4...列需要逆序

* 直接读取法：
索引和为偶数：
    元素在第一行，往右走
    元素在最后一列，往下走
    其他情况，往右上走
索引和为奇数：
    元素在第一列，往下走
    元素在最后一行，往右走
    其他情况，往左下走
"""
