"""
836. 矩形重叠

矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。

给出两个矩形，判断它们是否重叠并返回结果。

示例 1：
输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
输出：true

示例 2：
输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
输出：false

说明：
两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
矩形中的所有坐标都处于 -10^9 和 10^9 之间。
"""


class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        if (rec1 == rec2):
            return True

        x1 = [rec1[0], rec1[2]]
        x1.sort()
        y1 = [rec1[1], rec1[3]]
        y1.sort()

        x2 = [rec2[0], rec2[2]]
        x2.sort()
        y2 = [rec2[1], rec2[3]]
        y2.sort()

        # 中心点x，y相切距离
        px = (abs(x1[1] - x1[0]) + abs(x2[1] - x2[0])) / 2
        py = (abs(y1[1] - y1[0]) + abs(y2[1] - y2[0])) / 2

        # 中心点座标
        cx1 = (x1[1] - x1[0]) / 2 + x1[0]
        cy1 = (y1[1] - y1[0]) / 2 + y1[0]

        cx2 = (x2[1] - x2[0]) / 2 + x2[0]
        cy2 = (y2[1] - y2[0]) / 2 + y2[0]

        # 实际中心点在x，y轴的距离
        nowx = abs(cx1 - cx2)
        nowy = abs(cy1 - cy2)

        if (nowx < px and nowy < py):
            return True
        else:
            return False


s = Solution()
print(s.isRectangleOverlap([0, 0, 1, 1], [1, 0, 2, 1]))
print(s.isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
"""
此题解法：
* 两个矩形相交的判断依据是计算两个矩形的中心在x轴和y轴上的距离
* 如果x轴距离小于 矩形1的x/2 + 矩形2的x/2 并且在y轴的距离小于 矩形1的y/2 + 矩形2的y/2
  那么这两个矩形相交

    blX1, blY1, trX1, trY1 = rec1
    blX2, blY2, trX2, trY2 = rec2
    return ((blX1 < trX2) and (blX2 < trX1)) and  ((blY1 < trY2) and (blY2 < trY1))
"""
