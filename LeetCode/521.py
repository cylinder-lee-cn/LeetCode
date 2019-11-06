"""
521. 最长特殊序列 Ⅰ

给定两个字符串，你需要从这两个字符串中找出最长的特殊序列。
最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

子序列可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。
空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入为两个字符串，输出最长特殊序列的长度。如果不存在，则返回 -1。

示例 :
输入: "aba", "cdc"
输出: 3
解析: 最长特殊序列可为 "aba" (或 "cdc")

说明:
两个字符串长度均小于100。
字符串中的字符仅含有 'a'~'z'。
"""


class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        a_len = len(a)
        b_len = len(b)

        if (a_len != b_len):
            return max(a_len, b_len)
        else:
            if (a == b):
                return -1
            else:
                return a_len


s = Solution()
# print(s.findLUSlength('aba', 'cdc'))
# print(s.findLUSlength('aba', ''))
print(s.findLUSlength("aefawfawfawfaw", "aefawfeawfwafwaef"))
"""
此题解法：
* 如果A与B不等长，那长的那个就是最长特殊序列。因为长的那个肯定不可能是短的子序列。
* 如果A和B等长:
    1、 如果A==B，那么就没有特殊序列，就是-1
    2、 如果A!=B,那么各自就是各自的最长特殊序列，随便返回A或B的长度即可

一句话版本：
return -1 if a == b else max(len(a), len(b))
"""
