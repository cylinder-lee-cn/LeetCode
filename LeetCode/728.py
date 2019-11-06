"""
728. 自除数


自除数 是指可以被它包含的每一位数除尽的数。
例如，128 是一个自除数，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，列表的元素是边界（含边界）内所有的自除数。

示例 1：
输入
上边界left = 1, 下边界right = 22
输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

注意：
每个输入参数的边界满足 1 <= left <= right <= 10000。
"""


class Solution:
    def testi(self, n):
        nn = n
        while (n > 0):
            n, y = divmod(n, 10)
            if (y == 0 or nn % y != 0):
                return False

        return True

    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        rlist = []
        for i in range(left, right + 1):
            if (self.testi(i)):
                rlist.append(i)

        return rlist


s = Solution()
print(s.selfDividingNumbers(1, 100))
