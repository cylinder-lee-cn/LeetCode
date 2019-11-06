"""
29. 两数相除


给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。
返回被除数 dividend 除以除数 divisor 得到的商。

示例 1:
输入: dividend = 10, divisor = 3
输出: 3

示例 2:
输入: dividend = 7, divisor = -3
输出: -2
说明:

被除数和除数均为 32 位有符号整数。
除数不为 0。
假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。
本题中，如果除法结果溢出，则返回 2^31 − 1。
"""


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        signum = 1 if ((dividend > 0 and divisor > 0)
                       or (dividend < 0 and divisor < 0)) else -1

        dividend, divisor = abs(dividend), abs(divisor)

        if (dividend == 0):
            return 0

        if (dividend == divisor):
            return signum

        if (divisor == 1):
            if (-2147483648 <= signum * dividend <= 2147483647):
                return signum * dividend
            else:
                return 2147483647

        return signum * len(range(divisor, dividend + 1, divisor))


s = Solution()
print(s.divide(10, 3))
print(s.divide(7, -3))
"""
此题解法：
* 首先确定正负号，如果被除数、除数都是正的或都是负的，结果就是正的，反之是负的
* 排除特例，被除数是0，直接返回0
* 如果除数和被除数的绝对值相同，按照之前确定的符号返回 正负1
* 如果除数的绝对值==1，就要看被除数是否在 [−2^31,  2^31 − 1]，范围内，如果超了就返回2^31
* 最后，利用range(divisor, dividend + 1, divisor)的len就知道商了
  就是看被除数里有多少个除数，当然用while里做减法也可以
"""
