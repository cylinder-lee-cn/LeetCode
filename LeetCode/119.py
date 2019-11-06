"""
119. 杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 3
输出: [1,3,3,1]

进阶：
你可以优化你的算法到 O(k) 空间复杂度吗？

"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = []
        c = 1
        for j in range(rowIndex + 1):
            if (j == 0):
                r.append(1)
            elif (j > rowIndex / 2):
                r.append(r[rowIndex - j])
            else:
                c = c * (rowIndex + 1 - j) / j
                r.append(int(c))

        return r


s = Solution()
s.getRow(6)
"""
此题解法：

杨辉三角形的第k行第j个数的值为 C(k,j)=C(k,j-1)* (k-(j-1))/j
根据以上公式可以直接计算。
"""
