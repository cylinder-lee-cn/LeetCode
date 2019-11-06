"""
883. 三维形体投影面积

在 N * N 的网格中，我们放置了一些与 x，y，z 三轴对齐的 1 * 1 * 1 立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在单元格 (i, j) 上。
现在，我们查看这些立方体在 xy、yz 和 zx 平面上的投影。
投影就像影子，将三维形体映射到一个二维平面上。
在这里，从顶部、前面和侧面看立方体时，我们会看到“影子”。
返回所有三个投影的总面积。


示例 1：
输入：[[2]]
输出：5

示例 2：
输入：[[1,2],[3,4]]
输出：17
解释：
这里有该形体在三个轴对齐平面上的三个投影(“阴影部分”)。图883-1.png

示例 3：
输入：[[1,0],[0,2]]
输出：8

示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：14

示例 5：
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：21

提示：

1 <= grid.length = grid[0].length <= 50
0 <= grid[i][j] <= 50

"""


class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        sum_area = 0
        g_len = len(grid)
        for i in range(g_len):
            max_row = 0
            max_col = 0
            for j in range(g_len):
                v = grid[i][j]
                if (v > 0):
                    sum_area = sum_area + 1  # Z轴投影面积+1
                max_row = max(max_row, v)
                max_col = max(max_col, grid[j][i])
            sum_area = sum_area + max_row + max_col
        return sum_area


"""
此题解法：
* 一个座标上有方块，Z轴上会增加1
* 对于每个X值，高度最大的贡献投影面积，max(grid[x][0-y])
* 对于每个Y值，高度最大的贡献投影面积,max(grid[0-x][y])

        sum=0
        for row in grid:
            sum+=max(row)
            sum-=row.count(0)
        for col in zip(*grid):
            sum+=max(col)
        return sum+len(grid)*len(grid)
"""

s = Solution()
print(s.projectionArea([[2]]))
print(s.projectionArea([[2, 2, 2], [2, 1, 2], [2, 2, 2]]))
