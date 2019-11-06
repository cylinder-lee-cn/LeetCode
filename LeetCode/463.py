"""
463. 岛屿的周长


给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，
但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。
格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

示例 :
463-1.png

输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
输出: 16

解释: 它的周长是下面图片中的 16 个黄色的边：
"""


class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        count = 0
        for i in range(r):
            for j in range(c):
                if (grid[i][j] == 0):
                    continue
                count = count + 4
                if (i + 1 < r and grid[i + 1][j] == 1):
                    count = count - 2
                if (j + 1 < c and grid[i][j + 1] == 1):
                    count = count - 2
        return count


s = Solution()
print(
    s.islandPerimeter([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0,
                                                                  0]]))
"""
此题解法：
* 依次遍历每个方格，看看右方和下方是否有格子，如果有一个就减去2条边
"""
