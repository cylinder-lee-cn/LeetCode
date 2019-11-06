"""
67. 二进制求和
题目描述提示帮助提交记录社区讨论阅读解答
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
"""


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        prefix = '0b'

        a = prefix + a
        b = prefix + b

        return  format(int(a, 2) + int(b, 2),'b')


s = Solution()
print(s.addBinary('11', '1'))
print(s.addBinary('1010', '1011'))
print(s.addBinary('0', '0'))
