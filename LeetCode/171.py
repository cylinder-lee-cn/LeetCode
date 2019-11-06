"""
171. Excel表列序号

给定一个Excel表格中的列名称，返回其相应的列序号。

例如，
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...

示例 1:
输入: "A"
输出: 1

示例 2:
输入: "AB"
输出: 28

示例 3:
输入: "ZY"
输出: 701
"""


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
             'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14,
             'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21,
             'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
             }

        l = len(s)
        j = -1
        sum = 0
        for i in range(l):
            c = s[j]
            n = d[c]
            sum = sum + (n * 26 ** i)
            j = j - 1

        return sum

s = Solution()
print(s.titleToNumber('AZ'))

"""
解题思路, 这个是类26进制, A=1,B=2,C=3.....Y=25,Z=26
末尾位是X*26^0,倒数第二位是X*26^1,倒数第三位是X*26^2
"""
