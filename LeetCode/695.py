"""
695. 岛屿的最大面积

给定一个包含了一些 0 和 1的非空二维数组 grid ,
一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
"""


class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        direction = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(grid, x, y, m, n):
            if (x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == 0):
                return 0
            count = 1
            grid[x][y] = 0
            for i, j in direction:
                count = count + dfs(grid, x + i, y + j, m, n)
            return count

        result = 0
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if (grid[i][j] == 1):
                    result = max(result, dfs(grid, i, j, m, n))
        return result


s = Solution()
print(s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
print(
    s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
                        0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
                             0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
                                  0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0,
                        0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
                             0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
"""
此题解法：
* 典型的DFS，遍历矩阵，当1时就递归调用dfs。dfs每次遇到1就+1，并且将当前值置0
  dfs返回最后计数。
* 最后，将dfs的最大值返回

注意：
* 为了避免dfs重复计数，对于访问过的1，要马上置成0
* dfs是个递归，所以每层只需要返回本身的计数（1），以及其子递归返回的计数的和。
"""
