"""
840. 矩阵中的幻方

3 x 3 的幻方是一个填充有从 1 到 9 的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
给定一个由整数组成的 N × N 矩阵，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。

示例 1:
输入: [[4,3,8,4],
      [9,5,1,9],
      [2,7,6,2]]
输出: 1
解释:
下面的子矩阵是一个 3 x 3 的幻方：
438
951
276

而这一个不是：
384
519
762

总的来说，在本示例所给定的矩阵中只有一个 3 x 3 的幻方子矩阵。
提示:
1 <= grid.length = grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 3阶幻方只有如下8种形式，都是基本形式的镜像或旋转
        msquare3x = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]], [[6, 1, 8], [7, 5, 3],
                                                         [2, 9, 4]],
                     [[4, 9, 2], [3, 5, 7], [8, 1, 6]], [[2, 9, 4], [7, 5, 3],
                                                         [6, 1, 8]],
                     [[6, 7, 2], [1, 5, 9], [8, 3, 4]], [[8, 3, 4], [1, 5, 9],
                                                         [6, 7, 2]],
                     [[2, 7, 6], [9, 5, 1], [4, 3, 8]], [[4, 3, 8], [9, 5, 1],
                                                         [2, 7, 6]]]
        n = len(grid)
        m = len(grid[0])

        if (n < 3):
            return 0

        # 取3阶幻方需要从1，1 到 n-2，n-2，为中心点，上中下各取3个
        sumsquare = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                tmp = []
                if (grid[i][j] == 5):
                    tmp.append([
                        grid[i - 1][j - 1], grid[i - 1][j], grid[i - 1][j + 1]
                    ])
                    tmp.append([grid[i][j - 1], grid[i][j], grid[i][j + 1]])
                    tmp.append([
                        grid[i + 1][j - 1], grid[i + 1][j], grid[i + 1][j + 1]
                    ])
                    # print(tmp)
                    if (tmp in msquare3x):
                        sumsquare = sumsquare + 1
        return sumsquare


s = Solution()
print(s.numMagicSquaresInside([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]))
"""
此题解法：
使用查表方式来解决，3阶幻方只有8中形式。放入数组中。
当N>=3后，从（1，1)到（N-2，N-2）是3阶幻方的中心点，取上中下各三个元素构成3阶幻方。
三阶幻方中心点必定是5，如果是5的的话就检查一下三阶幻方是否在幻方表中即可
"""
