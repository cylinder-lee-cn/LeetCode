"""
812. 最大三角形面积

给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:

这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
812-1.png

注意:
3 <= points.length <= 50.
不存在重复的点。
 -50 <= points[i][j] <= 50.
结果误差值在 10^-6 以内都认为是正确答案。
"""


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        area = 0
        for x in points:
            for y in points:
                for z in points:
                    area = max(area,
                               (x[0] * y[1] + y[0] * z[1] + z[0] * x[1] -
                                x[0] * z[1] - y[0] * x[1] - z[0] * y[1]) * 0.5)

        return area


s = Solution()
print(s.largestTriangleArea([[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]))
"""
此题解法：暴力解法

三个点的座标
A(x1,y1),B(x2,y2),C(x3,y3)
面积
S=|x1y2+x2y3+x3y1-x1y3-x2y1-x3y2|

"""
