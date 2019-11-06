"""
441. 排列硬币
你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。

给定一个数字 n，找出可形成完整阶梯行的总行数。

n 是一个非负整数，并且在32位有符号整型的范围内。

示例 1:
n = 5
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤
因为第三行不完整，所以返回2.

示例 2:
n = 8
硬币可排列成以下几行:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
因为第四行不完整，所以返回3.
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if (n == 1):
        #     return 1

        i = 1
        while (n >= i):
            n = n - i
            i = i + 1

        return (i - 1)


s = Solution()
print(s.arrangeCoins(1))
print(s.arrangeCoins(3))
print(s.arrangeCoins(4))
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(100))
"""
此题解法：
1、使用循环，见上方代码
2、纯数学求法，使用开方计算，后续补上。
"""