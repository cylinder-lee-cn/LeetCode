"""
7. 反转整数
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2^31,  2^31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
"""
"""
自己的解法: 采用转换成字符串的方式进行反转,居然速度和使用纯数学的几乎一致.
"""


class Solutionlhb:
    def reverse(self, x):
        """
        :param x: int
        :return:  int
        """
        s = ""
        n = ""
        rev = 0

        if x == 0:
            rev = 0
            return rev
        elif x < 0:
            s = str(abs(x))
            n = "-"
        else:
            s = str(x)

        s = n + s[::-1].lstrip('0')

        rev = int(s)
        if rev > 2147483647 or rev < -2147483648:
            rev = 0

        return rev


"""
官网解法,用纯数学的方法进行数字的反转,不使用转换成字符串的办法.
* 十进制的数字除以十,余数就是这个数字的个位,商就是其余部分的数字, 比如 123 ÷ 10 = 12 ... 3
* 利用除法逐一的将末尾(个位)弹出

"""


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        symbol = False
        if x < 0:
            symbol = True
            x = -x

        while x != 0:
            y = divmod(x, 10)
            pop = y[1]
            x = y[0]
            rev = rev * 10 + pop

        if symbol:
            rev = -rev

        if rev > 2147483647 or rev < -2147483648:
            rev = 0
        return rev


S = Solution()
print(S.reverse(0))
print(S.reverse(1230))
print(S.reverse(32768))
print(S.reverse(-123))
