"""
415. 字符串相加

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。

"""


class Solution:
    def toInt(self, c):
        """
        :param c: str
        :return: int
        """
        ci = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        return ci[c]

    def add(self, a, b, f):
        """
        :param a: int
        :param b: int
        :param f: int (addone 0 or 1)
        :return c: int (addone)
        :return d: str
        """
        r = a + b + f
        if (r >= 10):
            c = 1
            d = r - 10
        else:
            c = 0
            d = r
        return c, str(d)

    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        l = max(l1, l2)
        addone = 0
        strsum = ''
        i = -1

        while (l > 0):
            if (i < -l1):
                a = 0
            else:
                a = self.toInt(num1[i])

            if (i < -l2):
                b = 0
            else:
                b = self.toInt(num2[i])
            addone, h = self.add(a, b, addone)
            strsum = h + strsum
            i = i - 1
            l = l - 1

        if (addone == 1):
            strsum = '1' + strsum

        return strsum


s = Solution()
print(s.addStrings('999', '99999'))
