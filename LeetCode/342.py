"""
342. 4的幂

给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。

示例 1:
输入: 16
输出: true

示例 2:
输入: 5
输出: false

进阶：
你能不使用循环或者递归来完成本题吗？

"""


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if (num <= 0):
            return False

        if (num & (num - 1) == 0):
            if (num & 0x55555555 == num):
                return True
            else:
                return False
        else:
            return False


"""
此题解法(经典解法):
4的幂首先是2的幂，因为4^n = (2^2)^n，所以4的幂的二进制同样只有一个1，
与2的幂不同的是，4的幂的二进制的1在偶数位上，所以判断一个数是不是4的幂的方式为：

1）首先判断是不是2的幂，使用 n & (n-1)
2）进一步判断与0x55555555的按位与结果，0x55555555是用十六进制表示的数，
其奇数位上全是1，偶数位上全是0，判断 n & 0x55555555
"""
