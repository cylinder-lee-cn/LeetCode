"""
371. 两整数之和


不使用运算符 + 和 - ​​​​​​​，计算两整数 ​​​​​​​a 、b ​​​​​​​之和。

示例 1:
输入: a = 1, b = 2
输出: 3

示例 2:
输入: a = -2, b = 3
输出: 1

"""


class Solution:
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        maxmask = 0x7fffffff
        mask = 0xffffffff
        while (b != 0):
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        return a if a <= maxmask else (a | ~mask)


s = Solution()
print(s.getSum(-2, 3))
"""
此题解法，使用二进制的位运算，a xor b 是位相加，不考虑进位，1+1 =0 0+0 = 0 1+0=1
(a and b) << 1 是进位
a+b 就是 （a xor b）+ （(a and b) << 1），如果(a and b) << 1 不为零就递归调用
也可以不用递归。
"""
