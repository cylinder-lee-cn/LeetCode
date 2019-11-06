"""
504. 七进制数
给定一个整数，将其转化为7进制，并以字符串形式输出。

示例 1:
输入: 100
输出: "202"

示例 2:
输入: -7
输出: "-10"
注意: 输入范围是 [-1e7, 1e7] 。

"""


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        if (num < 0):
            n = -num
        else:
            n = num

        while (n >= 7):
            n, y = divmod(n, 7)
            s = str(y) + s
        s = str(n) + s

        if (num < 0):
            s = '-' + s

        return s


s = Solution()
print(s.convertToBase7(7))
print(s.convertToBase7(-7))
print(s.convertToBase7(100))
print(s.convertToBase7(49))
print(s.convertToBase7(0))
