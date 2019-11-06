"""
661. 图片平滑器

包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，
平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:
输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

注意:
给定矩阵中的整数范围为 [0, 255]。
矩阵的长和宽的范围均为 [1, 150]。

"""


class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """

        new_m = []
        R = len(M)
        C = len(M[0])
        dir8 = [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1],
                [1, 1]]

        def vaildpoint(x, y, d):
            color = 0
            point = 0
            if ((0 <= x + d[0] < R) and (0 <= y + d[1] < C)):
                    color = M[x + d[0]][y + d[1]]
                    point = 1
            return [point, color]

        for r in range(R):
            tmp = []
            for c in range(C):
                all_color = M[r][c]
                all_point = 1
                for d in dir8:
                    p = vaildpoint(r, c, d)
                    all_point = all_point + p[0]
                    all_color = all_color + p[1]
                new_color = int(all_color / all_point)
                tmp.append(new_color)
            new_m.append(tmp)
        return (new_m)


s = Solution()
# print(s.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(
    s.imageSmoother([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13],
                     [14, 15, 16]]))
