"""
231. 2的幂

给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 20 = 1

示例 2:
输入: 16
输出: true
解释: 24 = 16

示例 3:
输入: 218
输出: false
"""


class Solution:
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if (bin(n).lstrip('0b').rstrip('0')=='1'):
        #     return True
        # else:
        #     return False

        # 经典解法:n如果是2的N次方,那二进制一定是100000....000 所以n-1就一定是011111...111, 这样的话位运算的逻辑"与"
        # n&n-1 就一定是0

        if (n <= 0):
            return False
        if (n & (n - 1) == 0):
            return True
        else:
            return False
