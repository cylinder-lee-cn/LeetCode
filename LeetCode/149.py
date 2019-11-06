""""
149. 直线上最多的点数

给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

示例 1:
输入: [[1,1],[2,2],[3,3]]
输出: 3
解释:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

示例 2:
输入: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出: 4
解释:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6

"""


# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        import collections

        def gcd(a, b):
            if (b == 0):
                return a
            return gcd(b, a % b)

        result = 0
        l_p = len(points)
        for i in range(l_p):
            # d = {(0, 0): 0}
            d = collections.defaultdict(int)
            duplicate = 1
            for j in range(i + 1, l_p):
                p1 = points[i]
                p2 = points[j]
                x1, y1 = p1
                x2, y2 = p2
                if (x1 == x2 and y1 == y2):
                    duplicate = duplicate + 1
                    continue
                dx = x2 - x1
                dy = y2 - y1
                dxy = gcd(dx, dy)
                # d[(dx / dxy, dy / dxy)] = d.get((dx / dxy, dy / dxy), 0) + 1
                d[(dx / dxy, dy / dxy)] = d[(dx / dxy, dy / dxy)] + 1
            # result = max(result, duplicate)
            result = max(result, (max(d.values()) if d else 0) + duplicate)
        return result

        # res = 0
        # l_p = len(points)

        # for i in range(l_p):
        #     duplicate = 1
        #     for j in range(i + 1, l_p):
        #         count = 0
        #         x1, y1 = points[i].x, points[i].y
        #         x2, y2 = points[j].x, points[j].y
        #         if (x1 == x2 and y1 == y2):
        #             duplicate = duplicate + 1
        #             continue
        #         for k in range(l_p):
        #             x3, y3 = points[k].x, points[k].y
        #             if (x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x2 * y1 -
        #                     x1 * y3 == 0):
        #                 count = count + 1
        #         res = max(res, count)
        #     res = max(res, duplicate)
        # return res


s = Solution()
print(s.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
"""
此题解法：
* 任意两点必定在一条直线上
* 问题变为，3点是否共线
* 3点共线常用的判断方法 A (ax,ay) ,B(bx,by),C(cx,cy)
1、斜率法，判断  (ay-by)/(ax-bx) == (cy-by)/(cx-bx)
   缺点：当 ax == bx 或 cx==bx 时需要特殊判断，注意使用gcd化简分子分母比较，不要使用浮点结果比较，可能会有误差
2、周长法，排序周长 AC > AB >BC
判断 AC == AB+BC
缺点：由于 sqrt  开方运算，导致结果不准确，不稳定，在三角形接近扁平时，结果有误差。

3.最优解法：面积法，判断 area(ABC) ==0
area(ABC) = 1/2 * ( AC X BC )  = 1/2 *((ax-cx)*(by-cy)-(bx-cx)*(ay-cy))
判断 (ax-cx)*(by-cy) == (bx-cx)*(ay-cy) 即可。
(ax-cx)*(by-cy)-(bx-cx)*(ay-cy)==0
"""
