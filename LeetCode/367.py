"""
367. 有效的完全平方数

给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

示例 1：
输入：16
输出：True

示例 2：
输入：14
输出：False

"""


class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while (num > 0):
            num = num - i
            i = i + 2

        return (num == 0)


s = Solution()
print(s.isPerfectSquare(14))
print(s.isPerfectSquare(0))
print(s.isPerfectSquare(2147483647))
print(s.isPerfectSquare(65536))
"""
此题解法：平方数有个推论，平方数是连续奇数的和。n的平方=1+3+5+7+...+（2n-1）
"""
