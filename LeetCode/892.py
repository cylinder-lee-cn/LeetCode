"""
892. 三维形体的表面积

在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
返回结果形体的总表面积。

示例 1：
输入：[[2]]
输出：10

示例 2：
输入：[[1,2],[3,4]]
输出：34

示例 3：
输入：[[1,0],[0,2]]
输出：16

示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32

示例 5：
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46

提示：
1 <= N <= 50
0 <= grid[i][j] <= 50
"""


class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_surface = 0
        for i, g in enumerate(grid):
            for j, v in enumerate(g):
                # print(i, j, v)
                sum_surface = sum_surface + v * 6  # 每个立方体有6面，先汇总一下
                if (v > 1):
                    sum_surface = sum_surface - (v - 1) * 2  # 减去z轴上遮挡的面

                if (i > 0):
                    sum_surface = sum_surface - min(
                        v, grid[i - 1][j]) * 2  # 减去x轴的遮挡面

                if (j > 0):
                    sum_surface = sum_surface - min(
                        v, grid[i][j - 1]) * 2  # 减去y轴的遮挡面

        return sum_surface


s = Solution()
print(s.surfaceArea([[1, 2], [3, 4]]))
print(s.surfaceArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
"""
此题解法：
* 一个正方体有6个面
* 在同一个座标上，每增加一个立方体就减少2个面（z轴）
* 水平方向上（x轴），如果左边有立方体，再减少2个面，要按照矮的算，高出来的就不被遮挡了
* 垂直方向上（y轴），如果下面有立方体，再减少2个面，要按照矮的算，高出来的就不被遮挡了

"""
