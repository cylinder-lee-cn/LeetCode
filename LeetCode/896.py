"""
896. 单调数列

如果数组是单调递增或单调递减的，那么它是单调的。
如果对于所有 i <= j，A[i] <= A[j]，那么数组 A 是单调递增的。
如果对于所有 i <= j，A[i]> = A[j]，那么数组 A 是单调递减的。
当给定的数组 A 是单调数组时返回 true，否则返回 false。

示例 1：
输入：[1,2,2,3]
输出：true

示例 2：
输入：[6,5,4,4]
输出：true

示例 3：
输入：[1,3,2]
输出：false

示例 4：
输入：[1,2,4,5]
输出：true

示例 5：
输入：[1,1,1]
输出：true

提示：
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
"""


class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        increase = True
        decrease = True

        la = len(A)
        if (la == 1):
            return True

        for i in range(1, la):
            if (A[i] - A[i - 1] >= 0):
                increase = increase & True
            else:
                increase = increase & False

        for i in range(1, la):
            if (A[i] - A[i - 1] <= 0):
                decrease = decrease & True
            else:
                decrease = decrease & False

        return (increase | decrease)


s = Solution()
print(s.isMonotonic([1, 1, 1]))
print(s.isMonotonic([1, 2, 2, 3]))
print(s.isMonotonic([6, 5, 4, 4]))
print(s.isMonotonic([1, 3, 2]))
"""
此题解法：依次判断相邻的两个元素是否满足相同的大小关系。

如下是非常python的写法：

return all(x>=y for x,y in zip(A,A[1:])) or all(x<=y for x,y in zip(A,A[1:]))

其中要注意all()函数和zip()函数的灵活使用
"""
