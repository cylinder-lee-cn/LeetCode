"""
976. 三角形的最大周长


给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
如果不能形成任何面积不为零的三角形，返回 0。

示例 1：
输入：[2,1,2]
输出：5

示例 2：
输入：[1,2,1]
输出：0

示例 3：
输入：[3,2,3,4]
输出：10

示例 4：
输入：[3,6,2,3]
输出：8

提示：
3 <= A.length <= 10000
1 <= A[i] <= 10^6
"""


class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        al = len(A)
        newA = sorted(A, reverse=True)

        for i in range(al - 2):
            if newA[i + 1] + newA[i + 2] > newA[i]:
                return newA[i] + newA[i + 1] + newA[i + 2]
        return 0


s = Solution()
print(s.largestPerimeter([2, 1, 2]))
print(s.largestPerimeter([1, 2, 1]))
print(s.largestPerimeter([3, 2, 3, 4]))
print(s.largestPerimeter([3, 6, 2, 3]))
