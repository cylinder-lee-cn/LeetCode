"""
941. 有效的山脉数组

给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[B.length - 1]

示例 1：
输入：[2,1]
输出：false

示例 2：
输入：[3,5,5]
输出：false

示例 3：
输入：[0,3,2,1]
输出：true

提示：
0 <= A.length <= 10000
0 <= A[i] <= 10000
"""


class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        a_l = len(A)
        left = 0
        right = a_l - 1
        if (a_l <= 2):
            return False

        while left < a_l - 1:
            if (A[left] < A[left + 1]):
                left = left + 1
            else:
                break
        while right > 0:
            if (A[right] < A[right - 1]):
                right = right - 1
            else:
                break
        return (left == right and 0 < left < a_l - 1)


s = Solution()
# print(s.validMountainArray([2, 1]))
# print(s.validMountainArray([3, 5, 5]))
# print(s.validMountainArray([0, 3, 2, 1]))
print(s.validMountainArray([0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 11]))
print(s.validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
"""
此题解法：
* 这个数组里的最大值索引必须在0 和 len(A)直接，而且数组以最大值为界，左边是递增、右边是递减
* 从左遍历数组，按照递增比较，找到最大值的索引，然后停止
* 从右边遍历数组，按照递增比较，找到最大值索引，然后停止
* 比较两个索引值是否相同，并且在0 到 len(A)之间，即为山脉数组
"""
