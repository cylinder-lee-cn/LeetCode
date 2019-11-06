"""
73. 矩阵置零
给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。请使用原地算法。

示例 1:
输入:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
输出:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

示例 2:
输入:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
输出:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

进阶:
一个直接的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个常数空间的解决方案吗？
"""


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        if (n < 1):
            return []
        m = len(matrix[0])

        r0 = [i for i, n in enumerate(matrix) if 0 in n]
        c0 = [j for j, m in enumerate(zip(*matrix)) if 0 in m]

        for r in r0:
            for c in range(m):
                matrix[r][c] = 0

        for c in c0:
            for r in range(n):
                matrix[r][c] = 0

        # print(matrix)
        return


s = Solution()
s.setZeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
s.setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])

"""
此题解法：
* 首先要找到matrix中所有0的所在的行，列。
* 然后根据行、列来更新matrix的值

据说是最快的：
        m=len(matrix)
        n=len(matrix[0])
        idx=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    idx.append((i,j))
                    
        while idx:
            i,j=idx.pop()
            matrix[i]=[0]*n
            for k in matrix:
                k[j]=0

"""
