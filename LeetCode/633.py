"""
633. 平方数之和

给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c。

示例1:
输入: 5
输出: True
解释: 1 * 1 + 2 * 2 = 5

示例2:
输入: 3
输出: False

"""


class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        upper = int(c**0.5)
        lower = 1
        if (c**0.5 == upper):
            return True

        while (lower <= upper):
            if (lower**2 + upper**2 > c):
                upper = upper - 1
            elif (lower**2 + upper**2 < c):
                lower = lower + 1
            else:
                return True
        return False


"""
此题解法：
* 上限是c开根号取整，下限是1，最极端的情况就是 c= 1^2+ a^2 , c^0.5=a 的情况。
* 如果upper^2+lower^2 > c，那么upper-1，如果<c，那么lower+1
"""

s = Solution()
print(s.judgeSquareSum(99))
print(s.judgeSquareSum(100))
