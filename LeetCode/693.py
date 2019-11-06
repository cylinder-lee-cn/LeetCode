"""
693. 交替位二进制数

给定一个正整数，检查他是否为交替位二进制数：换句话说，就是他的二进制数相邻的两个位数永不相等。

示例 1:
输入: 5
输出: True
解释:
5的二进制数是: 101

示例 2:
输入: 7
输出: False
解释:
7的二进制数是: 111

示例 3:
输入: 11
输出: False
解释:
11的二进制数是: 1011

示例 4:
输入: 10
输出: True
解释:
10的二进制数是: 1010
"""


class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if ((n + (n >> 1)) & (n + (n >> 1) + 1) == 0):
            return True
        else:
            return False


s = Solution()
print(s.hasAlternatingBits(5))
print(s.hasAlternatingBits(7))
print(s.hasAlternatingBits(11))
print(s.hasAlternatingBits(10))
"""
此题解法：0和1交错出现的数字右移一位，比如1010101会变成101010，
    二者相加变成1111111，在加上1就会变10000000，那么1111111&10000000=0；
    如果n=11,二进制为1011，n>>1=101,101+1011+1=10001这个数字和101取“与”是得不到0的
"""
